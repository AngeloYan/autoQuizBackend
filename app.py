from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def page():
    if request.method == "POST":
        x = request.get_json()
        topic = json.loads(x)["topic"]
        #q = getQuestions(topic)
    else:
        topic = "GET"
    return topic