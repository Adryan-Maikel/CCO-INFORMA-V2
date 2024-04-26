import { check_remove_row, check_form } from "../global.js"

check_remove_row("Operators", document.querySelectorAll("button.trash"))

check_form(
    "Operators",
    document.getElementById("form-operator"),
    [document.getElementById("operator"), document.getElementById("cracha")],
    document.getElementById("add-operator"),
    document.querySelectorAll("button.edit")
)

/*
const input = {
    operator: document.getElementById("operator"),
    cracha: document.getElementById("cracha")}

const buttons_edit = window.document.querySelectorAll("button.edit")
for(let button of buttons_edit){
    button.addEventListener("click", (event)=>{
        const button = event.target
        const row = button.id.replace("edit-row-", "")

        const _operator = document.getElementById(`operator-row-${row}`)
        const _cracha = document.getElementById(`cracha-row-${row}`)

        input.operator.value = _operator.textContent.trim()
        input.cracha.value = _cracha.textContent.trim()

        form_operator.setAttribute("action", `/edit-row/Operators/${row}`)
        form_operator.classList.add("open")
    })
}
*/