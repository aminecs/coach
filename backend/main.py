from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import emotions, conversations
import multiprocessing
import voice, stt

app = Flask(__name__)

param = None
onboarding_cnv = None
p1, p2 = None, None
# More permissive allowed origins configuration
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://*.ngrok-free.app",  # Updated pattern for ngrok URLs
    "https://*.ngrok.io",
    "http://localhost:*",        # Allow any local port
    "http://127.0.0.1:*"        # Allow any local IP port
]

# Enable CORS for Flask routes with more permissive settings
CORS(app, 
     resources={r"/*": {
         "origins": "*",  # More permissive for development
         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         "allow_headers": ["Content-Type", "Authorization", "X-Requested-With", "ngrok-skip-browser-warning"],
         "supports_credentials": True,  # Enable credentials
         "expose_headers": ["Content-Range", "X-Content-Range"]
     }})

# Initialize SocketIO with more permissive settings
socketio = SocketIO(app, 
                   cors_allowed_origins="*",
                   ping_timeout=60,
                   ping_interval=25,
                   async_mode='threading')  # Added async mode

@app.route("/")
def hello_world():
    global p1, p2
    name = request.args.get('name')
    goal = request.args.get('goal')

    print(name, goal)
    voice.speak("LET'S GET THIS RUN STARTING. START SLOW, FINISH STRONG. STAY HARD!")
    # Create communication queue for audio status
    status_queue = multiprocessing.Queue()
    
    # Create and start processes
    p1 = multiprocessing.Process(target=conversations.start_conversation, args=(status_queue,))
    p2 = multiprocessing.Process(target=emotions.get_llm_emotions_classification, args=(status_queue, name, goal))
    
    p1.start()
    p2.start()
    
    try:
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        print("\nShutting down...")
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()

    return "<p>Hello, World!</p>"

@app.route("/terminate")
def bye_world():
    global p1, p2
    p1.terminate()
    p2.terminate()
    p1.join()
    p2.join()
    return "<p>Goodbye, World!</p>"

@app.route('/api/video', methods=['GET'])
def video_endpoint():
    print("FUNCTION CALL WORKING - Video appears")
    socketio.emit('video')
    return "OK"

@app.after_request
def after_request(response):
    # Handle CORS headers for all responses
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 
                        'Content-Type, Authorization, X-Requested-With, ngrok-skip-browser-warning')
    response.headers.add('Access-Control-Allow-Methods', 
                        'GET, PUT, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/api/audio', methods=['GET'])
def audio_endpoint():
    global param
    param = request.args.get('param')
    # print("STARTING STT")
    # response = stt.stt(param)
    # print("response")
    return f"DONE - SET TO {param}"

@app.route('/api/start_onboarding', methods=['GET'])
def start_onboarding():
    global onboarding_cnv
    onboarding_cnv = conversations.onboarding()
    print("START: ", onboarding_cnv)
    return "ONBOARDING STARTED"

@app.route('/api/stop_onboarding', methods=['GET'])
def stop_onboarding():
    global onboarding_cnv
    print("STOP: ", onboarding_cnv)
    onboarding_cnv.end_session()
    return "ONBOARDING STOPPED"

@app.route('/api/help', methods=['GET'])
def help():
    global param
    print("HELP IS HERE")
    print("COACH IS HERE")
    if param == "name":
        voice.speak("What's your name?")
        response = stt.stt(param)
        socketio.emit('name', response);
        param = "other"
        return response
    elif param == "motivation":
        voice.speak("What's your motivation?")
        response = stt.stt(param)
        socketio.emit('motivation', response);
        return response
    else:
        return "DONE - WHY DID WE ASK FOR HELP?"
    

# @app.route('/api/onboarding', methods=['POST'])
# def onboarding():
#     print("ONBOARDING IS HERE")

if __name__ == "__main__":
    # Changed to listen on all interfaces
    socketio.run(app, 
                host="0.0.0.0",  # Changed from 127.0.0.1 to allow external access
                port=8200,
                allow_unsafe_werkzeug=True)  # Added for development
