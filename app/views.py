from flask import render_template, Flask
from app import *

@app.route("/")
def template_test():
    return render_template('template.html')
