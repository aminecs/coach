from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import emotions, conversations
import multiprocessing
import voice, stt

app = Flask(__name__)
allowed_origins = [
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:5173"
]

# Enable CORS for Flask routes
CORS(app, resources={
    r"/*": {
        "origins": allowed_origins,
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
        "supports_credentials": False,
        "expose_headers": ["Content-Range", "X-Content-Range"]
    }
})
socketio = SocketIO(app, cors_allowed_origins=allowed_origins)

@app.route("/")
def hello_world():
    name = request.args.get('name')
    goal = request.args.get('goal')

    print(name, goal)
    voice.speak("LET'S GET THIS RUN STARTING. START SLOW, FINISH STRONG. STAY HARD!")
    # Create communication queue for audio status
    status_queue = multiprocessing.Queue()
    
    # Create and start processes
    p1 = multiprocessing.Process(target=conversations.start_conversation, args=(status_queue,))
    p2 = multiprocessing.Process(target=emotions.get_llm_emotions_classification, args=(status_queue,))
    
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

@app.route('/api/video', methods=['GET'])
def video_endpoint():
    print("FUNCTION CALL WORKING - Video appears")
    socketio.emit('video')
    return 'ok'

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/api/audio', methods=['GET'])
def audio_endpoint():
    param = request.args.get('param')
    print("STARTING STT")
    response = stt.stt(param)
    print("response")
    return response

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000)
