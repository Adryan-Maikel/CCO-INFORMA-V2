const buttons_trash = window.document.querySelectorAll("button.button-trash")
for(let button of buttons_trash){
    button.addEventListener("click", (_)=>{window.location.href=`/del-row/${button.id.replace("del-row-", "")}`})
}

const form = {
    operator: document.getElementById("operator"),
    cracha: document.getElementById("cracha")
}

const buttons_edit = window.document.querySelectorAll("button.button-edit")
for(let button of buttons_edit){
    button.addEventListener("click", (event)=>{
        const button = event.target
        const tr = button.parentElement.parentElement
        const tds = tr.querySelectorAll("td")
        form["operator"].value = tds[1].textContent.trim()
        form["cracha"].value = tds[2].textContent.trim()
    })
}