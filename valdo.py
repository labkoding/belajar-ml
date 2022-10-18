from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route("/valdo/index")
def index():

    message= "Hayoloh!"
    return jsonify ({'message': message})