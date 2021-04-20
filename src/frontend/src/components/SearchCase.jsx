import React, { Component } from 'react';
import logo from '../logo.svg';
import '../App.css';
class SearchCase extends React.Component{
    handleSubmit(event){
        event.preventDefault();
        const data = new FormData(event.target);
        fetch('searchAPI',{
            method:'POST',
            body: data,
        }
        );
    }
    render(){
        return(
            <form>
                <label>
                    Case Number:
                </label>
                <input
                id="casenumber"
                name="searchcase"
                type="text"
                value="00000"
                >
                </input>
                <input type="submit" value="Search"/>
            </form>
        );
    }
}
export default SearchCase;
