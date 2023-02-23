from game import *
from flask import Flask, jsonify
from json import load

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def Items():
  with open("items.json", "r", encoding="utf-8") as f:
    data = load(f)
    return jsonify(data)

app.run()