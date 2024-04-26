import { check_remove_row, check_form } from "../global.js"

check_remove_row("sentidos", document.querySelectorAll("button.trash"))

check_form(
    "sentidos",
    document.querySelector("form"),
    [document.getElementById("sentido")],
    document.getElementById("add-sentido"),
    document.querySelectorAll("button.edit")
)
