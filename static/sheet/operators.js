import { check_remove_row, check_form } from "../global.js"

check_remove_row("operators", document.querySelectorAll("button.trash"))

check_form(
    "operators",
    document.getElementById("form-operator"),
    [document.getElementById("operator"), document.getElementById("cracha")],
    document.getElementById("add-operator"),
    document.querySelectorAll("button.edit")
)
