import React from "react";
import "../styles/Search.css"

class Search extends React.Component {
    componentDidMount() {
        document.title="EvictionSponge";
    }
    render() {
        return (
            <>
            <form>
                <div class="searchInputs">
                {/* <label for="firstName">First Name</label> */}
                <input class="searchField" type="text" id="firstName" name="firstName" required="true" placeholder="First Name"/>
                {/* <label for="middleName">Middle Name</label> */}
                <input class="searchField" type="text" id="middleName" name="middleName" placeholder="Middle Name(Opt.)"/>
                {/* <label for="lastName">Last Name</label> */}
                <input class="searchField" type="text" id="lastName" name="lastName" required="true" placeholder="Last Name"/>
                <input class="searchButton" type="submit" value="Search"/>
                </div>
            </form>
            </>
        );
    }
}

export default Search;