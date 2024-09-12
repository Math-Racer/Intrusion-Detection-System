from flask import Flask, render_template, request, jsonify
from app import app
from config import log_activity
from datetime import datetime
import pymongo

user_id = "Nizamudhin"
def Logging(user_id, page):
    log_activity.insert_one({
    'user_id': user_id,
    'page_accessed': page,
    'time_accessed': datetime.now()
    })

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/service/<int:service_id>")
def service(service_id):
    Logging(user_id,service_id)
    return render_template("service.html", service_id=service_id)

