import React, { useState, useEffect } from 'react';
import { Redirect, Route, Switch} from "react-router-dom";
import axios from '../node_modules/axios';
//import Header from "./Header";
import OECILogin from "./components/OeciLogin";
import navbar from "./components/navbar";
// import { Button, Navbar,Nav,Form,FormControl } from '../node_modules/react-bootstrap'

function App() {
  return (
  <>
  <OECILogin />
    <div className="App">
      <header className="App-header">
      </header>
    </div>
  </>

  );
}

export default App;
