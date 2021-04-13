import React, { useState, useEffect } from 'react';
import { Redirect, Route, Router, Switch} from "react-router-dom";
import axios from '../node_modules/axios';
import history from "./history";
import Landing from "./components/Landing";
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import Manual from "./components/Manual";
import Footer from "./components/Footer";
import Navbar from "./components/navbar";
import './styles/_globals.css'
import About from "./components/About";
import RecordSearch from "./components/RecordSearch";
import Search from "./components/Search";
// import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

function App() {
  return (
  <>
  <Router history={history}>
    <Navbar />
    <Switch>
      <Route component={Landing} exact={true} path="/" />
      <Route component={OECILogin} exact={true} path="/oeci-login" />
      <Route component={Manual} exact={true} path="/manual" />
      <Route component={About} exact={true} path="/about" />
      <Route component={Search} exact={true} path="/record-search" />
    </Switch>
    <Footer />
  </Router>
  </>

  );
}

export default App;
