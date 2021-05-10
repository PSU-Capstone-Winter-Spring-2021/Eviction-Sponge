import React from "react";


class Footer extends React.Component {

    /*constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
    };*/
    /*
    componentDidMount(){
        // document.title is the string in the tab, update it to reflect current component
        document.title = "footer"
    };
    */

    // HTML(?) for the component
    render() {
        return (
            <footer className = "container-lg navbar text-center fixed-bottom">
                <div className="row">
                    <div className="col-4">
                        <p className="row">
                            <a className="col-4" href="/">Home</a>
                            <a className="col-4" href="/about">About Us</a>
                            <a className="col-4" href="/manual">Manual</a>
                        </p>
                    </div>
                    <div className="col-4">
                        <p className="row">
                            <a className="col-4" href="/record-search">Search</a>
                            <a className="col-4" href="/partners">Partners</a>
                            <a className="col-4" href="/faq">FAQ</a>
                        </p>
                    </div>
                    <div className="col-4">
                        <p className="row">
                            <a className="col-4" href="/appendix">Appendix</a>
                            <a className="col-4" href="/accessibility">Accessibility Statement</a>
                            <a className="col-4" href="/privacy-policy">Privacy Policy</a>
                        </p>
                    </div>
                </div>
            </footer>
        )
    }


}

export default Footer;