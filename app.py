from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello from Python 10000!\n"
