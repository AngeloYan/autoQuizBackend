from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def generateQ():
        return "ok"