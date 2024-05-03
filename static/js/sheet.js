import {  } from "./global.js"

// const configurations = load_cookie_configurations()
// load_dark_mode(configurations)

const buttons = document.querySelectorAll(".buttons button")
for(const button of buttons){
    button.addEventListener("click", (event)=>{
        const row = event.target.id.replace("edit-", "");
        const inputs = document.querySelectorAll(`#row-${row} td input`)
        for(const input of inputs){
            input.removeAttribute("disabled")
            const div_buttons = document.querySelector(`#btns-r${row}`)
            div_buttons.classList.add("revel")
        }
    })
}