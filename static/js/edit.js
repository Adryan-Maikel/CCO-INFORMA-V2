import { } from "./global.js"

const iframe = document.querySelector("iframe")
const buttons = document.querySelectorAll("li button")
function remove_class_elements(list_elements, _class){
    for(const element of list_elements)
        element.parentElement.classList.remove(_class)
}
for(const button of buttons){
    button.addEventListener("click", (event)=>{
        remove_class_elements(buttons, "active")
        button.parentElement.classList.add("active")
        iframe.setAttribute("src", `/edit/${event.target.id}`);
    })
}