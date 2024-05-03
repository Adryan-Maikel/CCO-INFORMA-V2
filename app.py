from flask import Flask, render_template
from gsheets import INFORMATIONS as INFO

APP = Flask(__name__)


@APP.route("/")
def index() -> str:
    return render_template("index.html")


@APP.route("/edit/<table>")
def edit_table(table: str) -> str:
    if table == "sheets":
        return render_template("edit.html")
    ROWS = list(enumerate(INFO[table]["get"]()))
    COLS = [table.title()]
    if table == "operadores":
        ROWS = [[_id, *data] for _id, data in enumerate(INFO[table]["get"]())]
        COLS = ["Operadores", "Cracha"]

    return render_template("sheet.html", table=table.title(),
                           rows=ROWS, cols=COLS)


if __name__ == "__main__":
    APP.run(debug=True)
