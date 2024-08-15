""" The web application """

from flask import Flask
from flask import render_template

from delve import charclass

a = charclass.CharClass("donny", "pretty rare I guess", "man")

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Hello, Delve!!</h2>"

@app.route('/hello/')
def hello2():
    return render_template('info.html', c_class=a)

