import React, { useState, useEffect } from 'react';
import { Redirect, Route, Router, Switch } from "react-router-dom";
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
import FillFrom from "./components/FillForm"
import Search from "./components/Search";
import PartnersPage from "./components/PartnersPage";
import SearchPage from "./components/SearchPage";
// import FlashcardList from "./components/FlashcardList";
import Appendix from "./components/Appendix";
import SimpleCard from './components/SimpleCard';
import CreatSimpleCardList from './components/CreatSimpleCardList'
// import FaqPage from "./components/FaqPage";
import Accessibility from "./components/Accessibility";
import FooterPadding from "./components/FooterPadding"

//Example of FlashCardList
  // <div className="container">
  //     <FlashcardList flashcards={flashcards} />
  //   </div>
// import SearchCase from './components/searchcase';
// import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

function App() {
  return (
  <>
  <Router history={history}>
    <Navbar />
    <Switch>
      <Route component={CreatSimpleCardList} exact={true} path="/cards_demo" />
      <Route component={Landing} exact={true} path="/" />
      <Route component={OECILogin} exact={true} path="/oeci-login" />
      <Route component={Manual} exact={true} path="/manual" />
      <Route component={About} exact={true} path="/about" />
      <Route component={Search} exact={true} path="/record-search" />
      <Route component={FillFrom} exact={true} path="/fill-form" />
      <Route component={PartnersPage} exact={true} path="/partners" />
      <Route component={Appendix} exact={true} path="/appendix" />
      <Route component={Accessibility} exact={true} path="/accessibility" />
    </Switch>
    <Footer />
    
  </Router>
  </>

  );
}

window.onbeforeunload = function() {
  localStorage.clear();
}

export default App;
