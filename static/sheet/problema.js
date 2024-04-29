import { check_remove_row, check_form } from "../global.js"

check_remove_row("problemas", document.querySelectorAll("button.trash"))

check_form(
    "problemas",
    document.querySelector("form"),
    [document.getElementById("problema")],
    document.getElementById("add-problema"),
    document.querySelectorAll("button.edit")
)
