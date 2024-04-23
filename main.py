"""

"""

from flask import Flask, render_template, request
from gsheets import get_operators

OPERATORS = get_operators()
APP = Flask(__name__)


@APP.route("/")
def index():
    return render_template("index.html")


@APP.route("/login")
def login():
    operator = request.cookies.get("operator", "")
    if operator and operator in OPERATORS:
        return render_template("home.html", operator=operator)
    return render_template("login.html", _class="")


@APP.route("/home", methods=["POST"])
def home():
    operator = request.form.get("operator", "")
    if operator in OPERATORS:
        return render_template("home.html", operator=operator)
    return render_template("login.html", _class="error")


if __name__ == "__main__":
    APP.run(debug=True)
