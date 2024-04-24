export function set_cookie_operator(operator=""){
    const date = new Date()
    date.setMonth(date.getMonth() + 1)
    document.cookie = `operator=${operator}; expires=Thu, ${date.getDate()} ${date.getMonth()} ${date.getFullYear()} 00:00:00 UTC; path=/`
}