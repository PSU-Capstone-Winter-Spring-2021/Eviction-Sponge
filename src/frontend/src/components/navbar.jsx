import React from "react";
import { Link } from "react-router-dom";
// import Logo from "../Logo";
import { Button, Navbar,Nav,Form,FormControl } from 'react-bootstrap'

export default class navbar extends React.Component{
    componentDidMount(){
        document.title = "Navbar - RecordSponge";
    }
    render(){
        return(
          <div className="bg-white shadow">
          <nav 
            className="mw8 relative center flex flex-wrap justify-between pa3"
            aria-label="Primary"
          >
            <div className="logo mb4 mb0-ns">
              {/* <Link to="/" aria-label="Home">
                <Logo />
              </Link> */}
            </div>
            <div className="mt5 mt2-ns">
              <Link
                to="/manual"
                className="link hover-blue f5 fw6 pv2 ph0 ph3-ns mr4-ns"
              >
                Manual
              </Link>
              <Link
                to="/record-search"
                className="absolute top-1 right-1 static-ns bg-blue white bg-animate hover-bg-dark-blue f5 fw6 br2 pv2 ph3"
              >
                Search
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