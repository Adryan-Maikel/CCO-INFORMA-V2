"""

"""

from flask import Flask, render_template, request  # , redirect
from gsheets import get_operators

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html", classList="")


@app.route("/home", methods=["POST"])
def home():
    operator = request.form.get("operator", "")
    if operator in get_operators():
        return render_template("home.html")
    return render_template("login.html", classList="error")


if __name__ == "__main__":
    app.run(debug=True)
