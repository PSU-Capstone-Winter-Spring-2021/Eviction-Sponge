import React, { useState, useEffect } from 'react';
import { Redirect, Route, Router, Switch} from "react-router-dom";
import axios from '../node_modules/axios';
import history from "./history";
import Landing from "./components/Landing";
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import PartnersTable from "./components/PartnersTable";
import Footer from "./components/Footer";
import navbar from "./components/navbar";
// import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

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
      </header>
  <PartnersTable>
    
  </PartnersTable>
    </div>
    <Footer />
  </>

  );
}

export default App;
