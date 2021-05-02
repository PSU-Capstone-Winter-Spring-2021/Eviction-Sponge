import React from "react";
import axios from "axios";
import "../styles/Search.css";
import {checkOeciRedirect, redirectLogin, removeCookie} from "../cookieService";
import CreatSimpleCardList from './CreatSimpleCardList';

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            Submitted: false,
            Found: false,
            Loaded: false,
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
        this.setState({Loaded: false, Found: false})
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
<<<<<<< HEAD
                this.setState({Loaded: true});
                console.log(res.data);
                this.setState({Results: res.data, Found: true});
=======
                this.state.Found = true;
                this.setState({Results: res});
                console.log(res);
                if(res.status == 401 || res.status == 500){
                    redirectLogin();
                }
>>>>>>> 61e80b69fa2d80720f264ef1c51c5382f410a8f8
            }
        }, reason => {
            redirectLogin();
            removeCookie();
        })
<<<<<<< HEAD
        if(this.state.Results.length === 0) {
            this.setState({Found: false})
        }
=======

>>>>>>> 61e80b69fa2d80720f264ef1c51c5382f410a8f8
    }

    render() {
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
                    !this.state.Found && 
                    !this.state.Loaded &&<p class="loadingText"> Loading...</p>
                }
                {this.state.Submitted &&  
                    this.state.Loaded &&
                    !this.state.Found &&<p class="notFoundText"> No results Found</p>
                }
                </div>
            </form>
            {this.state.Submitted &&
                    this.state.Found && <div>{CreatSimpleCardList(this.state.Results)}</div>}
            </>
        );
    }
}

export default Search;