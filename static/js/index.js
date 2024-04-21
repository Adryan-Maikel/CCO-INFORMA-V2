const status_icon = document.querySelector("#i-wifi > .fa-minus")
function check_connection(){
    if(navigator.onLine){
        status_icon.style.display = "none"
        return
    }
    status_icon.style.display = "block"
}
check_connection()
window.addEventListener("online", check_connection)
window.addEventListener("offline", check_connection)