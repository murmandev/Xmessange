import time 
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! <br><a href='/status'>Статус</a>"

@app.route("/status")
def hello():
    return {
        'status': True,
        'name': 'Xmessage Messanger',
        'time': time.time()
        'time2': time.asctime()
        'time3': datetime.now()
    }


app.run()
