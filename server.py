import time 
from datetime import datetime

from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! <br><a href='/status'>Статус</a>"

@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Xmessage Messanger',
        'time': time.time(),
        'time2': time.asctime(),
        'time3': datetime.now()
    }

@app.route("/send_message", methods=['POST'])
def send_message():
    data = request.json
    print(data)
    text = data['text']
    author = data['author']

    if isinstance(text, str) and isinstance(author, str):
        db.append({
            'text': text,
            'author': author,
            'time': time.time()
        })
        return Response({'ok': True})
    else:
        return Response({'ok': False}, 400)


@app.route("/get_messages")
def get_messages():
    return {'messages': db}


app.run()
