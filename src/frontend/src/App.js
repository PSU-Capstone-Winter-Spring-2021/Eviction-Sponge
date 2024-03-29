import React, { useState, useEffect } from 'react';
import CacheBuster from 'react-cache-buster';
import {version} from '../package.json';
import { Redirect, Route, Router, Switch } from "react-router-dom";
import axios from '../node_modules/axios';
import history from "./history";
import Landing from "./components/Landing";
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import Manual from "./components/Manual";
import Footer from "./components/Footer";
import Navbar from "./components/navbar";
import "./index.css";
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
import FooterPadding from "./components/FooterPadding";
import PrivacyPolicy from "./components/PrivacyPolicy";
import DemoPage from "./components/DemoPage"

function App() {
  const isProduction = process.env.NODE_ENV === 'production';
  const redirect = () => <Redirect to="/" />;
  return (
  <>
  <CacheBuster
  currentVersion={version}
  isEnabled={isProduction}
  isVerboseMode={true}
  >
  <Router history={history}>
    <Navbar />
    <Switch>
      <Route component={DemoPage} exact={true} path="/cards_demo" />
      <Route component={Landing} exact={true} path="/" />
      <Route component={OECILogin} exact={true} path="/oeci-login" />
      <Route component={Manual} exact={true} path="/manual" />
      <Route component={About} exact={true} path="/about" />
      <Route component={Search} exact={true} path="/record-search" />
      <Route component={FillFrom} exact={true} path="/fill-form" />
      <Route component={PartnersPage} exact={true} path="/partners" />
      <Route component={Appendix} exact={true} path="/appendix" />
      <Route component={Accessibility} exact={true} path="/accessibility" />
      <Route component={PrivacyPolicy} exact={true} path="/privacy-policy" />
      <Route render={redirect} />
    </Switch>
    <Footer />
  </Router>
  </CacheBuster>
  </>

  );
}

window.onbeforeunload = function() {
  localStorage.clear();
}

export default App;
