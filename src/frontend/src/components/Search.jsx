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
        document.title="Search Records - EvictionSponge";
        let local = [];
        if(local = localStorage.getItem('Results')) {
            let res = JSON.parse(local)
            if (res.Expiration < Date.now()) {
                localStorage.removeItem('Results');
            }
            else
            {
                this.setState({
                Results: res.Results,
                Submitted: true,
                Found: true,
                });
            }
        }
    }

    async handleSubmit(e) {
        e.preventDefault();
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
                this.setState({Loaded: true});
                console.log(res.data);
                this.setState({Results: res.data, Found: true});
                localStorage.setItem('Results', JSON.stringify({
                    Expiration: Date.now() + 600000, //This should set expiration for search to 10 minutes.
                    Results: res.data}))
                    console.log("expiration time: " + Date.now()+600000)
                if(res.status == 401 || res.status == 500){
                    redirectLogin();
                }
            }
        }, reason => {
            redirectLogin();
            removeCookie();
        })
        if(this.state.Results.length === 0) {
            this.setState({Found: false})
        }
    }

    render() {
        return (
                <main className="container-fluid search-container bg-light p-sm-3 pt-1">
                    <form className="row justify-content-center bg-light">
                        <div className="row searchInputs col-sm-9 border p-md-3 p-1">
                            <div className="col-sm-4 px-1">
                                <label for="firstName">First Name*:</label>
                                <input className="searchField w-100" type="text" id="firstName" name="firstName" required="true" placeholder="First Name"/>
                            </div>
                            <div className="col-sm-4 px-1">
                                <label for="middleName">Middle Name:</label>
                                <input className="searchField w-100" type="text" id="middleName" name="middleName" placeholder="Middle Name(Opt.)"/>
                            </div>
                            <div className="col-sm-4 px-1">
                                <label for="lastName">Last Name*:</label>
                                <input className="searchField w-100" type="text" id="lastName" name="lastName" required="true" placeholder="Last Name"/>
                            </div>
                            <p className="col-12 text-right">* indicates a required field</p>
                            <div className="col-sm-4 col-12 px-1">
                                <input className="w-100 searchButton btn" type="submit" value="Search" onClick={this.handleSubmit.bind(this)}/>
                            </div>


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
            </main>
        );
    }
}

export default Search;