from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(port=5000)