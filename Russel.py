from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/russel/hello-world')
def api_hello_world():
    first_name = "Russel"
    last_name = "Pangkey"
    age = 17
    return jsonify({
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        })

@app.route('/russel/user')
def api_user():
    id = "123456789"
    first_name = "Russel"
    last_name = "Pangkey"
    age = 17
    email = "Russelpangkey77@gmail.com"
    return jsonify({
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'email': email,
        })