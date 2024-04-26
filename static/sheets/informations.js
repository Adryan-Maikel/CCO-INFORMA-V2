const buttons = document.querySelectorAll("button")
const iframe = document.querySelector("iframe")

const lis = document.querySelectorAll("ul>li")
function reset_class_li(_class, button){
    for(const li of lis)
        if(li.classList.contains(_class))
            li.classList.remove(_class)
    button.parentNode.classList.add(_class)
}

for(const button of buttons){
    button.addEventListener("click", (_)=>{
        reset_class_li("selected", button)
        iframe.setAttribute("src", `/sheet/${button.id}`)
    })
}
