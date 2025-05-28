from flask import Flask
from os import getcwd

app = Flask(__name__)


@app.route("/")
def index():
    with open("index.html", "r") as file:
        return file.read()
    
@app.route("/langs")
def langs():
    with open("langs/index.html", "r") as file:
        return file.read()
    
@app.route("/langs/python")
def python():
    with open("langs/python/index.html", "r") as file:
        return file.read()
    
@app.route("/langs/js")
def js():
    with open("langs/js/index.html", "r") as file:
        return file.read()

@app.route("/langs/c")
def c():
    with open("langs/c/index.html") as file:
        return file.read()
    
@app.route("/langs/css")
def css():
    with open("langs/css/index.html") as file:
        return file.read()

app.run(port=8080)