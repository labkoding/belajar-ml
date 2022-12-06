from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)

@app.route('/Yonathan/api', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})