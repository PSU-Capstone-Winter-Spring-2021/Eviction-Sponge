import React from "react";


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
            <div>
                <p>
                    <h1>
                        Introduction
                    </h1>
                    <a>
                        introduction text
                    </a>
                </p>
                <p>
                    <h1>
                        General Info
                    </h1>
                    <a>
                        general info text
                    </a>
                </p>
                <p>
                    <h1>
                        How to Use EvictionSponge
                    </h1>
                    <a>
                        how to use text
                    </a>
                </p>
                <p>
                    <h1>
                        Assumptions
                    </h1>
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
            /*
            <textarea>
                Step 1: Hit Search, if it's been implemented
                Step 2: Login
                Step 3: Search yourself
                Step 4: ???
                Step 5: Profit!
            </textarea>*/
        )
    }
}

export default Manual;