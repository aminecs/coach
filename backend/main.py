from flask import Flask, request
import emotions, conversations
import multiprocessing
import voice, stt

app = Flask(__name__)

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
    return "FUNCTION CALL - Video appears"

@app.route('/api/audio', methods=['GET'])
def audio_endpoint():
    param = request.args.get('param')
    print("STARTING STT")
    response = stt.stt(param)
    print("response")
    return response

if __name__ == "__main__":
    app.run()
