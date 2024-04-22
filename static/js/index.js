// Configurações gerais
function update_cookie_config(configs){
    const DATA = JSON.stringify(configs)
    const DATE = new Date()
    DATE.setTime(DATE.getTime() + (8000 * 24 * 60 * 60 * 1000))
    document.cookie = `configurations=${DATA};expires=${DATE.toUTCString()};path=/`
}
function load_cookie_config(){
    var configurations = {"dark_mode": false, "show_seconds": false}
    const cookies = decodeURIComponent(document.cookie).split(';')
    for(var i = 0; i < cookies.length; i++){
        var cookie = cookies[i].trim();
        if(cookie.indexOf("configurations=") === 0)
            return JSON.parse(cookie.substring("configurations=".length, cookie.length))    
    }
    update_cookie_config(configurations)
    return configurations
}
var configurations = load_cookie_config()

const input_show_seconds = window.document.getElementById("show_seconds")
input_show_seconds.checked = configurations["show_seconds"]
input_show_seconds.addEventListener("click", (events)=>{
    configurations["show_seconds"] = events.target.checked
    update_cookie_config(configurations)
})

const input_dark_mode = window.document.getElementById("dark_mode")
input_dark_mode.checked = configurations["dark_mode"]
input_dark_mode.addEventListener("click", (events)=>{
    configurations["dark_mode"] = events.target.checked
    update_cookie_config(configurations)
})

const menu = window.document.querySelector(".menu-options")
window.document.getElementById("open-menu").addEventListener("click", ()=>menu.classList.toggle("open"))
const clock = window.document.getElementById("relogio")
function set_hour(){
    const date = new Date()
    const hour = date.getHours()
    const min = date.getMinutes()
    const sec = date.getSeconds()
    
    var format_hour = `${hour<10?"0"+hour:hour}:${min<10?"0"+min:min}`
    clock.textContent = !configurations["show_seconds"]?format_hour:`${format_hour}:${sec<10?"0"+sec:sec}`
}
set_hour()
setInterval(set_hour, 1000)

// Icone de wi-fi
const status_icon = document.querySelector("#i-wifi > .fa-minus")
function check_connection(){
    status_icon.style.display = navigator.onLine? "none": "block"
}
check_connection()
window.addEventListener("online", check_connection)
window.addEventListener("offline", check_connection)