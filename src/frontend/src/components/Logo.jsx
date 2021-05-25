import React from "react";
import logoImage from "../logo.png";

console.log(logoImage);

function Logo(){
    return <img src={logoImage} alt="Logo" width="100" height="100" />;
}

export default Logo;