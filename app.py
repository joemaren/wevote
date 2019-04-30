# flask
from flask import Flask, render_template, request

# poll model
from models.models import Poll

# sqlachemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Date, Integer, Column, String

# uuid
import uuid


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/polls")
def polls():
    uid = uuid.uuid4()
    question = request.args.get('question')
    options = [request.args.get('option1'),request.args.get('option2'), request.args.get('option3'), request.args.get('option4')]
    poll = Poll(uid, question, options)
    print(poll.uid, poll.question, poll.options)

    return render_template('polls.html')
