from flask import Flask, render_template, request, session, redirect,Response
import datetime
from datetime import timedelta
import sqlite3
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def api():
    if request.method == "GET":
        return redirect("가짜 웹훅 링크")
    else:
        url = os.environ['WEBHOOK']
        obj = request.get_json()
        requests.post(url, json = obj)
        return " "

app.run()