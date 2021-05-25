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
            <div>
                <div className="footer-padding d-none d-md-block">
                </div>
                <footer className = "border-top d-md-none navbar justify-content-center">
                    <div className="row">
                        <div className="col-12 p-0">
                            <p className="row m-0 border-bottom">
                                <a className="col-4" href="/">Home</a>
                                <a className="col-4" href="/about">About Us</a>
                                <a className="col-4" href="/manual">Manual</a>
                            </p>
                        </div>
                        <div className="col-12 p-0">
                            <p className="row m-0 border-bottom">
                                <a className="col-4" href="/record-search">Search</a>
                                <a className="col-4" href="/partners">Partners</a>
                                <a className="col-4" href="/appendix">Appendix</a>
                                {/* <a className="col-4" href="/faq">FAQ</a> */}
                            </p>
                        </div>
                        <div className="col-12 p-0">
                            <p className="row m-0">
                                <a className="col-4" href="/accessibility">Accessibility Statement</a>
                                <a className="col-4" href="/privacy-policy">Privacy Policy</a>
                            </p>
                        </div>
                    </div>
                </footer>
                <footer className = "border-top d-none d-md-flex navbar justify-content-center fixed-bottom">
                    <div className="row">
                        <div className="col-12 p-0">
                            <p className="row">
                                <a className="col" href="/">Home</a>
                                <a className="col" href="/about">About Us</a>
                                <a className="col" href="/manual">Manual</a>
                                <a className="col" href="/record-search">Search</a>
                                <a className="col" href="/partners">Partners</a>
                                <a className="col" href="/appendix">Appendix</a>
                                <a className="col" href="/accessibility">Accessibility Statement</a>
                                <a className="col" href="/privacy-policy">Privacy Policy</a>
                            </p>
                        </div>
                    </div>
                </footer>
            </div>
        )
    }


}

export default Footer;