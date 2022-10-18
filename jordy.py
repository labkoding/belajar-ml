from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/jordy/index')
def index():
    message = "hello world"
    return jsonify ({'message': message})