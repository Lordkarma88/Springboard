from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def home():
    return render_template("home.html", survey=survey)


@app.route("/q/<int:n>")
def question_page(n):
    question = survey.questions[n-1]

    return render_template("question.html", q=question, n=n)
