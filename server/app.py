# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def entry():
    return "/entry"




