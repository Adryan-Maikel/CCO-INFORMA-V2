function check_remove_row(sheet, buttons){
    for(let button of buttons){
        button.addEventListener("click", (_)=>
            window.location.href=`/del-row/${sheet}/${button.id.replace("del-row-", "")}`)
    }
}

function check_form(sheet, form, inputs, button_open, buttons_edit){
    button_open.addEventListener("click", (_)=>{
        form.setAttribute("action", `/add-row/${sheet}`)
        form.classList.add("open")
        inputs[0].focus()
    })
    for(let button of buttons_edit){
        button.addEventListener("click", (event)=>{
            const row = event.target.id.replace("edit-row-", "")
            for(let input of inputs)
                input.value = document.getElementById(`${input.name}-row-${row}`).textContent.trim()
            
            form.setAttribute("action", `/edit-row/${sheet}/${row}`)
            form.classList.add("open")
        })
    }
    form.addEventListener("submit", (event)=>{
        event.preventDefault()

        for(let input of inputs)
            if(input.value == "")
                return input.focus()

        form.submit()
    })
    form.addEventListener("reset", (_)=>{
        form.setAttribute("action", "#")
        form.classList.remove("open")
    })
}

export { check_remove_row, check_form }