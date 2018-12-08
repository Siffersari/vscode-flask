from flask import Flask, render_template
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Flask!"

@app.route('/hello/<name>')
def hello_there(name):    
    return render_template("hello_there.html", name=name, date=datetime.now())