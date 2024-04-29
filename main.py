"""

"""

from flask import Flask, render_template, request
from gsheets import OPERATORS, informations

APP = Flask(__name__)


@APP.route("/")
def index():
    return render_template("index.html")


@APP.route("/sheet/<name>")
def sheet(name: str):
    match name:
        case "edit":
            return render_template("sheet/informations.html")
        case "operators":
            VALUES = enumerate(OPERATORS["get"]())
            return render_template("sheet/operators.html", rows=VALUES)
        case "ocorrencias":
            VALUES = enumerate(informations("Ocorrências")["get"]())
            return render_template("sheet/ocorrencias.html", rows=VALUES)
        case "problemas":
            VALUES = enumerate(informations("Problemas")["get"]())
            return render_template("sheet/problemas.html", rows=VALUES)
        case "sentidos":
            VALUES = enumerate(informations("Sentidos")["get"]())
            return render_template("sheet/sentidos.html", rows=VALUES)
        case "_":
            return "<html><body>Erro</body></html>"


@APP.route("/add-row/<sheet>", methods=["POST"])
def add_row(sheet):
    match sheet:
        case "operators":
            OPERATORS["add"]([request.form["operator"],
                              int(request.form["cracha"])])
            NEW_VALUES = enumerate(OPERATORS["get"]())
            # return render_template("sheet/operators.html", rows=NEW_VALUES)
        case "ocorrencias":
            informations("Ocorrências")["add"]([request.form["ocorrencia"]])
            NEW_VALUES = enumerate(informations("Ocorrências")["get"]())
            # return render_template("sheet/ocorrencias.html", rows=NEW_VALUES)
        case "problemas":
            informations("Problemas")["add"]([request.form["problema"]])
            NEW_VALUES = enumerate(informations("Problemas")["get"]())
            # return render_template("sheet/problemas.html", rows=NEW_VALUES)
        case "sentidos":
            informations("Sentidos")["add"]([request.form["sentido"]])
            NEW_VALUES = enumerate(informations("Sentidos")["get"]())
            # return render_template("sheet/sentidos.html", rows=NEW_VALUES)

    return render_template(f"sheet/{sheet}.html", rows=NEW_VALUES)


@APP.route("/del-row/<sheet>/<id_row>")
def del_row(sheet, id_row: str):
    if not id_row.isnumeric():
        return "Erro"

    match sheet:
        case "operators":
            OPERATORS["del"](int(id_row))
            NEW_VALUES = enumerate(OPERATORS["get"]())
            return render_template("sheet/operators.html", rows=NEW_VALUES)
        case "ocorrencias":
            informations("Ocorrências")["del"](int(id_row))
            NEW_VALUES = enumerate(informations("Ocorrências")["get"]())
            return render_template("sheet/ocorrencias.html", rows=NEW_VALUES)
        case "problemas":
            informations("Problemas")["del"](int(id_row))
            NEW_VALUES = enumerate(informations("Problemas")["get"]())
            return render_template("sheet/problemas.html", rows=NEW_VALUES)
        case "sentidos":
            informations("Sentidos")["del"](int(id_row))
            NEW_VALUES = enumerate(informations("Sentidos")["get"]())
            return render_template("sheet/sentidos.html", rows=NEW_VALUES)


@APP.route("/edit-row/<sheet>/<id_row>", methods=["POST"])
def edit_row(sheet, id_row: str):
    if not id_row.isnumeric():
        return "Erro"

    if sheet == "operators":
        OPERATORS["update"]([request.form["operator"],
                            int(request.form["cracha"])], int(id_row) + 1)
        NEW_VALUES = enumerate(OPERATORS["get"]())
        return render_template("sheet/operators.html", rows=NEW_VALUES)
    if sheet == "ocorrencias":
        informations("Ocorrências")["update"]([request.form["ocorrencia"]],
                                              int(id_row) + 1)
        NEW_VALUES = enumerate(informations("Ocorrências")["get"]())
        return render_template("sheet/ocorrencias.html", rows=NEW_VALUES)
    if sheet == "problemas":
        informations("Problemas")["update"]([request.form["problema"]],
                                            int(id_row) + 1)
        NEW_VALUES = enumerate(informations("Problemas")["get"]())
        return render_template("sheet/problemas.html", rows=NEW_VALUES)
    if sheet == "sentidos":
        informations("Sentidos")["update"]([request.form["sentido"]],
                                           int(id_row) + 1)
        NEW_VALUES = enumerate(informations("Sentidos")["get"]())
        return render_template("sheet/sentidos.html", rows=NEW_VALUES)


if __name__ == "__main__":
    APP.run(debug=True)
