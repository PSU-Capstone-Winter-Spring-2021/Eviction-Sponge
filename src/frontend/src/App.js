import React, { useState, useEffect } from 'react';
import { Redirect, Route, Router, Switch} from "react-router-dom";
import axios from '../node_modules/axios';
import history from "./history";
import Landing from "./components/Landing";
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import PartnersTable from "./components/PartnersTable";
import Footer from "./components/Footer";
import Navbar from "./components/navbar";
import Search from "./components/Search";
import SearchPage from "./components/SearchPage";
// import SearchCase from './components/searchcase';
// import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

function App() {
  return (
  <>
  <Router history={history}>
    <Navbar/>
    <Switch>
      <Route component={Landing} exact={true} path="/" />
      <Route component={OECILogin} exact={true} path="/Login"/>
      <Route component={Search} exact={true} path="/Search"/>
    </Switch>
    <SearchPage />
    {/* // <SearchCase/> */}
  </Router>
    <Footer />
  </>

  );
}

export default App;
