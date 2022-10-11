from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/yonathan/hello-world')
def api_hello_world():
    first_name = "Yonathan"
    last_name = "Tjiptomo"
    age = 21
    return jsonify({
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    })