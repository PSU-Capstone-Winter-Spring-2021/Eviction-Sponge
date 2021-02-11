import React, { useState, useEffect } from 'react';
import { Redirect, Route, Router, Switch} from "react-router-dom";
import axios from '../node_modules/axios';
import history from "./history";
import Landing from "./components/Landing";
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

function App() {
  return (
  <>
  <Router history={history}>
    <Switch>
      <Route component={Landing} exact={true} path="/" />
    </Switch>
  </Router>
  <OECILogin />
    <div className="App">
      <header className="App-header">
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="#home">Home</Nav.Link>
      <Nav.Link href="#features">Features</Nav.Link>
      <Nav.Link href="#pricing">Pricing</Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-info">Search</Button>
    </Form>
  </Navbar>
  <br />
  <Navbar bg="primary" variant="dark">
    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="#home">Home</Nav.Link>
      <Nav.Link href="#features">Features</Nav.Link>
      <Nav.Link href="#pricing">Pricing</Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-light">Search</Button>
    </Form>
  </Navbar>

  <br />
  <Navbar bg="light" variant="light">
    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="#home">Home</Nav.Link>
      <Nav.Link href="#features">Features</Nav.Link>
      <Nav.Link href="#pricing">Pricing</Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-primary">Search</Button>
    </Form>
  </Navbar>
      </header>
    </div>
  </>
  );
}

export default App;
