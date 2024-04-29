import { check_remove_row, check_form } from "../global.js"

check_remove_row("ocorrencias", document.querySelectorAll("button.trash"))

check_form(
    "ocorrencias",
    document.querySelector("form"),
    [document.getElementById("ocorrencia")],
    document.getElementById("add-ocorrencia"),
    document.querySelectorAll("button.edit")
)
