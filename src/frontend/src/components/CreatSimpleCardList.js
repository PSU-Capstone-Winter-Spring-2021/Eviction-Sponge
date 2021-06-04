import React from 'react';
import SimpleCard from './SimpleCard';

export default function CreatSimpleCardList(results){
    var rows = []
    let len = results.length
    // console.log("from Create Simple Card List:");
    // console.log(results);
    //results.map((result) => rows.push(<SimpleCard res ={[result]}/>));
    // rows.map((row) => <p>{row}</p>);
    return <div>{results.map((result) =>(<SimpleCard res ={result}/>))}</div>;
}
