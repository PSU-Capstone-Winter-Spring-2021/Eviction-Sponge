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
            <textarea>
                Step 1: Hit Search, if it's been implemented
                Step 2: Login
                Step 3: Search yourself
                Step 4: ???
                Step 5: Profit!
            </textarea>
        )
    }
}

export default Manual;