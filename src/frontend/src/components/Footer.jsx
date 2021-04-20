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
            <footer className = "container-lg bg-light text-left">
                <p className="row">
                    <a className="col-2" href="/">Home</a>
                    <a className="col-2" href="/about">About Us</a>
                </p>
                <p className="row">
                    <a className="col-2" href="/manual">Manual</a>
                    <a className="col-2" href="/record-search">Search</a>
                </p>
                <p className="row">
                    <a className="col-2" href="/partners">Partners</a>
                    <a className="col-2" href="/etc">Etc</a>
                </p>
            </footer>
        )
    }


}

export default Footer;