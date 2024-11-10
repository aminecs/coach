from flask import Flask
import emotions, conversations
import multiprocessing

app = Flask(__name__)

@app.route("/")
def hello_world():
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

if __name__ == "__main__":
    app.run()