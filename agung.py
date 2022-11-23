from unicodedata import name
from xml.parsers.expat import model
from flask import Flask
from flask import jsonify
from keras.models import load_model
from PTL import Image, ImageOps 
import numpy as np


app = Flask(__name__)
@app.route("/agung/upload-gambar")
def api_hello_world():
    first_name= "agung"
    last_name= "kurniawan"
    age = 22
    return jsonify ({
        'first_name' : first_name,
        'last_name' : last_name,
          })

@app.route('agung/absensi')
def api_user():

model = load_model('keras_model.h5')

