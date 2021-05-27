import history from "./history";



export function checkCookieExists(cookieName){
    var name = cookieName + "=";
    if(document.cookie.split(';').some((item)=>item.trim().startsWith(name))){
        console.log('The cookie "' + cookieName + '" exists');
        return true;
    }
    console.log('The cookie "' + cookieName + '" does not exists')
    return false;
}

export function removeCookie(){
    document.cookie = "remember_token=; max-age=0;";
    document.cookie = "oeci_token=; max-age=0;";
    document.cookie = "is_admin=; max-age=0;";
}

export function hasOeciToken(){
    return checkCookieExists("oeci_token");
}

export function isAdmin(){
    return document.cookie.includes("is_admin");
}

export function checkOeciRedirect(isDemo){
    if(!isDemo && !hasOeciToken()){
        history.push("/oeci-login");
    }
}

export function validateCookie(){
    return;
}

export function redirectSearch(){
    history.push("/record-search");
}

export function redirectLogin(){
    history.push("/oeci-login");
}