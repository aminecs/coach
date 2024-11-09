from flask import Flask
import emotions, conversations
import multiprocessing

app = Flask(__name__)

@app.route("/")
def hello_world():
    thread_1 = multiprocessing.Process(target=conversations.start_conversation)
    thread_1.start()
    thread_2 = multiprocessing.Process(target=emotions.get_llm_emotions_classification)
    thread_2.start()

    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()