from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello World"

app.run(port=4495)