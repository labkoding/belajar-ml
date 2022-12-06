from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/agung/hello")
def api_hello_world():
    message= "hello"
    return jsonify ({'message': message