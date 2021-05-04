import React from "react";
import axios from "axios";
import "../styles/Search.css";
import {checkOeciRedirect, redirectLogin, removeCookie} from "../cookieService";

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            Submitted: false,
            Found: false,
            Results: [],
        };
    }
    componentDidMount() {
        this.props.demo || checkOeciRedirect();
        document.title="EvictionSponge";
    }

    async handleSubmit(e) {
        e.preventDefault();
        //let url= "/search";
        //check if cookie exists (user deleted cookie)
        checkOeciRedirect();
        let firstName = String(document.getElementById("firstName").value);
        let middleName = String(document.getElementById("middleName").value);
        let lastName = String(document.getElementById("lastName").value);
        let postName = {
            "first_name" : firstName,
            "last_name": lastName,
            "middle_name": middleName
        }
        console.log("clicked, names: " + postName.first_name + " " + postName.last_name +", " + postName.middle_name);
        this.setState({Submitted: true});
        await axios.post("/search", postName).then(res => {
            if(res !== null) {
                this.state.Found = true;
                this.setState({Results: res});
                console.log(res);
                if(res.status == 401 || res.status == 500){
                    redirectLogin();
                }
            }
        }, reason => {
            redirectLogin();
            removeCookie();
        })

    }

    render() {
        const notFound = <p class="notFoundText">No results found.</p>
        return (
            <>
            <form class="bg-light">
                <div class="searchInputs">
                {/* <label for="firstName">First Name</label> */}
                <input class="searchField" type="text" id="firstName" name="firstName" required="true" placeholder="First Name"/>
                {/* <label for="middleName">Middle Name</label> */}
                <input class="searchField" type="text" id="middleName" name="middleName" placeholder="Middle Name(Opt.)"/>
                {/* <label for="lastName">Last Name</label> */}
                <input class="searchField" type="text" id="lastName" name="lastName" required="true" placeholder="Last Name"/>
                <input class="searchButton" type="submit" value="Search" onClick={this.handleSubmit.bind(this)}/>
                {this.state.Submitted && 
                    !this.state.Found && <span class="notFoundText"> No results Found</span>
                }
                </div>
            </form>
            </>
        );
    }
}

export default Search;