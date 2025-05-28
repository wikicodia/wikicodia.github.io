from flask import Flask, send_from_directory
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
    
@app.route("/favicon.ico")
def favicon():
    with open("favicon.ico", "rb") as file:
        return send_from_directory(app.root_path, "favicon.ico")

app.run(port=8080)