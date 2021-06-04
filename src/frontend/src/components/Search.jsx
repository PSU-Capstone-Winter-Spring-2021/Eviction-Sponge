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
                this.setState({
                Results: res.Results,
                Submitted: true,
                Found: true,
                });
            }
        }

    async handleSubmit(e) {
        e.preventDefault();
        //check if cookie exists (user deleted cookie)
        checkOeciRedirect(this.props.demo);
        this.setState({Loaded: false, Found: false})
        let firstName = String(document.getElementById("firstName").value);
        let middleName = String(document.getElementById("middleName").value);
        let lastName = String(document.getElementById("lastName").value);
        let postName = {
            "first_name" : firstName,
            "last_name": lastName,
            "middle_name": middleName
        }
        this.setState({Submitted: true});
        if(this.props.demo){
            await axios.post("/demo", postName).then(res => {
                if(res !== null) {
                    this.setState({Loaded: true});
                    // console.log(res.data);
                    this.setState({Results: res.data, Found: true});
                    // if(res.status == 401 || res.status == 500){
                    //     redirectLogin();
                    // }
                }
            })
        }
        else{
            
            await axios.post("/search", postName).then(res => {

            if(res !== null) {
                this.setState({Loaded: true});
                // console.log(res.data);
                this.setState({Results: res.data, Found: true});
                localStorage.setItem('Results', JSON.stringify({
                    Expiration: Date.now() + 600000, //This should set expiration for search to 10 minutes.
                    Results: res.data}))
                if(res.status == 401 || res.status == 500){
                    redirectLogin();
                }
            }
            }, reason => {
                redirectLogin();
                removeCookie();
            })
        }
        if(this.state.Results.length === 0) {
            this.setState({Found: false})
        }
    }



    render() {
        return (
                <main className="container-fluid search-container bg-light p-sm-3 pt-1">
                    <h1 className="hidden">Eviction Case Search</h1>
                    <form className="row justify-content-center bg-light">
                        <div className="row searchInputs col-sm-9 border p-md-3 p-1">
                            <div className="col-sm-4 px-1">
                                <label htmlFor="firstName">First Name*:</label>
                                <input className="searchField w-100" type="text" id="firstName" name="firstName" required={true} placeholder="First Name"/>
                            </div>
                            <div className="col-sm-4 px-1">
                                <label htmlFor="middleName">Middle Name:</label>
                                <input className="searchField w-100" type="text" id="middleName" name="middleName" placeholder="Middle Name(Opt.)"/>
                            </div>
                            <div className="col-sm-4 px-1">
                                <label htmlFor="lastName">Last Name*:</label>
                                <input className="searchField w-100" type="text" id="lastName" name="lastName" required={true} placeholder="Last Name"/>
                            </div>
                            <p className="col-12 text-right">* indicates a required field</p>
                            <div className="col-sm-4 col-12 px-1">
                                <input className="w-100 searchButton btn" type="submit" value="Search" onClick={this.handleSubmit.bind(this)}/>
                            </div>


                        {this.state.Submitted &&
                            !this.state.Found &&
                            !this.state.Loaded &&<p className="loadingText"> Loading...</p>
                        }
                        {this.state.Submitted &&
                            this.state.Loaded &&
                            !this.state.Found &&<p className="notFoundText"> No results Found</p>
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