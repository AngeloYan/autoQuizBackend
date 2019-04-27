from flask import Flask, request
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/",methods=["GET","POST"])
@cross_origin()
def page():
    # response.headers.add('Access-Control-Allow-Origin','*')
    if request.method == "POST":
        #x = request.get_json()
        x = request.form.get("topic")
        #x = request.get_data()
        print(x)
        #topic = json.loads(x)["topic"]
        #q = getQuestions(topic)
    #else:
        #topic = "GET"
    #topic.headers.add('Access-Control-Allow-Origin','*')
    #return topic
    return 'ok'