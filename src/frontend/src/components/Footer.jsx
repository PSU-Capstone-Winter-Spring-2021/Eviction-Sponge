                                import React from "react";


class Footer extends React.Component {

    /*constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
    };*/

    componentDidMount(){
        // document.title is the string in the tab, update it to reflect current component
        document.title = "footer"
    };

    // HTML(?) for the component
    render() {
        return (
            <footer className = "footer">
                <p>
                    <a href="/">Home</a>
                    <a href="/about">About Us</a>
                    <a href="/partners">Partners</a>
                    <a href="/manual">Manual</a>
                    <a href="/record-search">Search</a>
                    <a href="/etc">Etc</a>
                </p>
            </footer>
        )
    }


}

export default Footer;