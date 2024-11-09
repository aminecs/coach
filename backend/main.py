from flask import Flask
import emotions, conversations
import multiprocessing

app = Flask(__name__)

@app.route("/")
def hello_world():
    control_event = multiprocessing.Event()
    control_event.set()

    p1 = multiprocessing.Process(target=conversations.start_conversation)
    p1.start()
    p2 = multiprocessing.Process(target=emotions.get_llm_emotions_classification, args=(control_event,))
    p2.start()

    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()