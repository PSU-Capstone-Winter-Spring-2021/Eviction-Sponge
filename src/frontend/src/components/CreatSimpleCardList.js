import React from 'react';
import SimpleCard from './SimpleCard';

export default function CreatSimpleCardList(){
    var rows = []
    for(var i = 0; i < 11;i++){
        rows.push(<SimpleCard/>)
    }
    return rows;
}
