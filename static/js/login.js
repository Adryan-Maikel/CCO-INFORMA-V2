const operator = window.document.getElementById("operator")
window.document.querySelector("form").addEventListener("submit", (events)=>{
    // events.preventDefault()
    document.cookie = `operator=${operator.value}; expires=Thu, 18 Dec 2025 12:00:00 UTC; path=/`
    events.submitter
})