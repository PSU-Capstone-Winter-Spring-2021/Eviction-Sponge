import React from "react";
import { Link } from "react-router-dom";
import Logo from "./Logo";
import { Button, Navbar,Nav,Form,FormControl } from 'react-bootstrap'
import "bootstrap/dist/css/bootstrap.css";


export default class navbar extends React.Component{
    render(){
        return(
        <div className="container-fluid pb-2 bg-white border-bottom">
          <nav className="row justify-content-center align-items-end"
            aria-label="Primary"
          >
            <Link className="col-lg-4" to="/" aria-label="Home">
              <Logo />
            </Link>
            <div className= "col-lg-4">
              <Link
                to="/manual"
                className="mx-2"
              >
                Manual
              </Link>
              <Link
                to="/record-search"
                className="mx-2"
              >
                <Button className = "button">Search</Button>
              </Link>
            </div>
          </nav>
        </div>
        )
    }
}