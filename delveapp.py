""" The web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    """ Shows the homepage """
    return "<h2>Hello, Delve!!</h2>"

@app.route("/character/<id>")
def show_character(id):
    """ Shows a character sheet """
    return render_template("charsheet.html")
