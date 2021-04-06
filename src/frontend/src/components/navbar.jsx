import React from "react";
import { Link } from "react-router-dom";
import Logo from "./Logo";
import { Button, Navbar,Nav,Form,FormControl } from 'react-bootstrap'

export default class navbar extends React.Component{
    render(){
        return(
          <div>
          <nav className="navbar"
            aria-label="Primary"
          >
            <div className="logo">
              {<Link to="/" aria-label="Home">
                <Logo />
              </Link>}
              <h1 className = "pageTitle">EvictionSponge</h1>
            </div>
            <div className = "navButtons">
              <Link
                to="/manual"
              >
                Manual
              </Link>
              <Link
                to="/record-search"
              >
                <Button className = "button">Search</Button>
              </Link>
            </div>
          </nav>
        </div>
          // <main>
          // <Navbar bg="light" variant="light">
          //   <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          //   <Nav className="mr-auto">
          //     <Nav.Link href="#home">Home</Nav.Link>
          //     <Nav.Link href="#Menu">Menu</Nav.Link>
          //     {/* <Nav.Link href="#Search">Search</Nav.Link> */}
          //   </Nav>
          //   <Form inline>
          //     <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          //     <Button variant="outline-primary">Search</Button>
          //   </Form>
          // </Navbar>
          // </main>
        )
    }
}