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

export function decodeCookie(cookieName){
    var name = cookieName + "=";
    var decodedCookie = decodeURIComponent(document.cookie).split(';');
    for(var i = 0; i < decodedCookie.length; i++){
        var c = decodedCookie[i];
        while (c.charAt[0] == ' '){
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0){
            return true;
        }
    }
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

export function checkOeciRedirect(){
    if(!hasOeciToken()){
        history.push("/oeci-login");
    }
}

