from flask import Flask, jsonify
from flask_cors import CORS
from src.main import *


app = Flask("shopping-cart")
CORS(app)

@app.route("/", methods=["GET"])
def hello_world():
    return "hello"

@app.route("/shopping-cart", methods=["GET"])
def list_of_dict():
    result = shopping_list_as_prepare_to_jsonify()
    return jsonify(result)   