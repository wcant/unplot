import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/file-upload')
def file_upload(): 
    if app.request.method == 'POST':
        pass #handle file
    else:
        pass

@app.route('/')
def index(name=None):
    return app.render_template('index.html', name=name)
