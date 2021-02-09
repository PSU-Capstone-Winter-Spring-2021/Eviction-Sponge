import React, { useState, useEffect } from 'react';
import { Redirect, Route, Switch} from "react-router-dom";
import axios from 'axios';
import Header from "./Header";

function App() {
	  const [data, setData] = useState({ hits: [] });
	 
	  useEffect(async () => {
		      const result = await axios(
			            'https://hn.algolia.com/api/v1/search?query=redux',
			          );
		   
		      setData(result.data);
		    });
	 
	  return (
		      <ul>
		        {data.hits.map(item => (
				        <li key={item.objectID}>
				          <a href={item.url}>{item.title}</a>
				        </li>
				      ))}
		      </ul>
		    );
}
 
export default App;
