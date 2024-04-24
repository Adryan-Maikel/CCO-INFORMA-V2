import { set_cookie_operator } from "./scripts.js"

const operator = window.document.getElementById("operator")
window.document.querySelector("form").addEventListener("submit", (events)=>{
    // events.preventDefault()
    set_cookie_operator(operator.value)
    events.submitter
})