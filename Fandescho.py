from flask import Flask
from flask import jsonifyx

app = Flask(__name__)
@app.route('/Fandescho/hello-world')
def api_hello_world():
    first_name = "Fandescho"
    last_name = "Malalantang"
    age = 21
    return  jsonify({
        'firs_name' : first_name,
        'last_name' : last_name,
        'age' : age,
    })