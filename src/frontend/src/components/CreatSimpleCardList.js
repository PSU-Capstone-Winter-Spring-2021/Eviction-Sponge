import React from 'react';
import SimpleCard from './SimpleCard';
import SearchBar from "./SearchBar";
import DemoPage from './DemoPage';
export default function CreatSimpleCardList(){
    var rows = []
    rows.push(<DemoPage/>)
    rows.push(<SearchBar/>)
    for(var i = 0; i < 11;i++){
        rows.push(<SimpleCard/>)
    }
    return rows;
}
