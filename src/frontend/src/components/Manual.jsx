import React from "react";
import "bootstrap/dist/css/bootstrap.css";

class Manual extends React.Component {

    constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
    };

    componentDidMount(){
        // document.title is the string in the tab, update it to reflect current component
        document.title = "Manual"
    };

    // HTML(?) for the component
    render() {
        return (
         <div className="container bg-light w-100 m-0 mw-100 px-0">
                <div className="row px-3">
                    <div className="col col-9 border text-left">
                        <div className="">
                            <h2>
                                Introduction
                            </h2>
                            <p className="font-weight-light">
                            EvictionSponge is a web application used to facilitate the expungement process for evictions that occured in Oregon. It is built by a team of students at PSU for their capstone project and is based on the RecordSponge project by Code for PDX. The codebase is published under an open source MIT license.
        <br />This Manual explains how EvictionSponge is used and the process of expunging eviction records. 
                            </p>
                        </div>
                        <div className="">
                            <h2>
                                General Info
                            </h2>
                            <a>
                                general info text
                            </a>
                        </div>
                        <p>
                            <h2>
                                How to Use EvictionSponge
                            </h2>
                            <a>
                                how to use text
                            </a>
                        </p>
                        <p>
                            <h2>
                                Assumptions
                            </h2>
                            <a>
                                <h2>
                                    assumption 1
                                </h2>
                                text
                                <h2>
                                    assumption 2
                                </h2>
                                text
                            </a>
                        </p>
                    </div>
                    <div className="col-3 border">
                        
                    </div>
                </div>
            </div>
        )
    }
}

export default Manual;