import React from 'react';
import { Button, Navbar,Nav,Form,FormControl } from 'react-bootstrap'
const SearchBar = ({keyword,setKeyword}) => {
  const BarStyling = {width:"20rem",background:"#F2F1F9", border:"none", padding:"0.5rem"};
  return (
    <div>
    <input 
     style={BarStyling}
     key="random1"
     value={keyword}
     placeholder={"Search By Case Number"}
    />
    <Button className = "button">Search</Button>
    {/* <input class="searchButton" type="submit" value="Search"/> */}
    </div>
  );
}

export default SearchBar