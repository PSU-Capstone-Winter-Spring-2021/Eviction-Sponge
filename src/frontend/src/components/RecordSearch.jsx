import React from "react";
import { checkOeciRedirect } from "../cookieService";

class RecordSearch extends React.Component{

    componentDidMount(){
        this.props.demo || checkOeciRedirect();
        document.title = "Search Records - EvictionSponge";
    }

    render(){
        return(
            <h1>temp page</h1>
        )
    }
}

export default RecordSearch;