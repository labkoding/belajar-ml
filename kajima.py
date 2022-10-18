from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    message =  "<p>Hello world!<p>"
    return jsonify({'message': message})