# demo flask app
from flask import Flask, render_template
from flask import send_from_directory


app = Flask(__name__)


@app.route('/assets/<path:path>')
def send_report(path):
    # Using request args for path will expose you to directory traversal attacks
    print("The path is: ", path)
    return send_from_directory('assets', path)

@app.route('/')
def hello_world():
    # render hello template
    return render_template('hello.html')