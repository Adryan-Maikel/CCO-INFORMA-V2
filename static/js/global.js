const create_cookie_configurations=()=>{
    const configurations=JSON.stringify({cursor_personalizado: true,dark_mode: false});
    const expires="Fri, 31 Dec 9999 23:59:59 GMT";
    document.cookie=`configurations=${configurations}; expires=${expires}; path=/`;
    return JSON.parse(decodeURIComponent(configurations));
}
const load_cookie_configurations=()=>{
    var cookie=document.cookie.split(';').find(cookie => cookie.trim().startsWith('configurations='));
    if (cookie) {
        var configurations=cookie.split('=')[1];
        return JSON.parse(decodeURIComponent(configurations));
    } else {
        return create_cookie_configurations();
    }
}
const update_cookie_configurations=(new_configurations)=>{
    const expires="Fri, 31 Dec 9999 23:59:59 GMT";
    document.cookie=`configurations=${JSON.stringify(new_configurations)}; expires=${expires}; path=/`
    window.location.reload();
}
const toogle_option_menu=(configurations, option)=>{
    configurations[option]=!configurations[option];
    return configurations;
}

/* DARK-MODE */
const load_dark_mode=(configurations)=>{
    if(configurations.dark_mode){
        document.documentElement.style.setProperty("--white", "#1F1A2A")
        document.documentElement.style.setProperty("--dark", "#EDEDED")
    }else{
        document.documentElement.style.setProperty("--white", "#EDEDED")
        document.documentElement.style.setProperty("--dark", "#1F1A2A")
    }
}

const CURSORS = {
    default:"/static/assets/normal.cur",danger:"/static/assets/unavailable.cur",link:"/static/assets/link.cur",
    move:"/static/assets/move.cur",scroll_x:"/static/assets/horizontal.cur",scroll_y:"/static/assets/vertical.cur"
}
/* CURSOR */
const buttons = document.querySelectorAll("button")
const inputs = document.querySelectorAll("input")

const load_cursor = (configurations) => {
    // document.addEventListener("contextmenu", (event)=>event.preventDefault())
    if(!configurations.cursor_personalizado)return;

    document.documentElement.style.setProperty("--cursor", `url(${CURSORS.default}), auto`);
    document.addEventListener("mousedown", (event)=>{if(event.button!=0)event.preventDefault()});
    for(const button of buttons){
        button.addEventListener("mouseenter", ()=>{
            document.documentElement.style.setProperty("--cursor", `url(${CURSORS.link}), auto`);
        })
        button.addEventListener("mouseout", ()=>
            document.documentElement.style.setProperty("--cursor", `url(${CURSORS.default}), auto`))
    }
    for(const input of inputs){
        input.addEventListener("mouseenter", (event)=>{
            if(event.target.disabled)
                document.documentElement.style.setProperty("--cursor", `url(${CURSORS.danger}), auto`)
            
        })
        input.addEventListener("mouseout", ()=>{
            document.documentElement.style.setProperty("--cursor", `url(${CURSORS.default}), auto`)            
        })
    }
}


const configurations = load_cookie_configurations()
load_dark_mode(configurations)
load_cursor(configurations)

export{ load_cookie_configurations, toogle_option_menu, load_dark_mode, update_cookie_configurations, load_cursor }