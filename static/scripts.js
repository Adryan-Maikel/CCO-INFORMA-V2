const buttons_trash = window.document.querySelectorAll("button.trash")
for(let button of buttons_trash){
    button.addEventListener("click", (_)=>{
        window.location.href=`/del-row/Operators/${button.id.replace("del-row-", "")}`
    })
}

const input = {
    operator: document.getElementById("operator"),
    cracha: document.getElementById("cracha")
}

const form_operator = document.getElementById("form-operator")
const button_add_operator = document.getElementById("add-operator")

button_add_operator.addEventListener("click", (_)=>{
    form_operator.setAttribute("action", "/add-row/Operators")
    form_operator.classList.add("open")
})
form_operator.addEventListener("submit", (event)=>{
    event.preventDefault()
    if(input.operator.value == ""){
        input.operator.focus()
        return
    }
    if(input.cracha.value == ""){
        input.cracha.focus()
        return
    }

    form_operator.submit()
})
form_operator.addEventListener("reset", (_)=>{
    form_operator.setAttribute("action", "#")
    form_operator.classList.remove("open")
})

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


