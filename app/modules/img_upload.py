# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from jinja2 import TemplateNotFound

# Import the database object from the main app module
from app import db

# Import module models
#?

# Define the blueprint: 'img_upload', set its url prefix: app.url/img_upload
img_upload = Blueprint('img_upload', __name__)

# Set the route and accpeted methods
@img_upload.route('/')
def img_upload():
    return render_template("/img_upload.html")


