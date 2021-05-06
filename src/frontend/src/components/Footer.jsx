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
            <footer className = "container-lg text-left center-block">
                <div className="row">
                    {/* <div className="col-4"> */}
                        {/* <p className="row"> */}
                            <a className="col" href="/">Home</a>
                            {/* <a className="col-md-4" href="/">Home</a> */}
                            <a className="col" href="/about">About Us</a>
                            <a className="col" href="/manual">Manual</a>
                        {/* </p> */}
                        {/* </p>
                    </div>
                    <div className="col-4">*/}
                        {/* <p className="row">  */}
                            <a className="col" href="/record-search">Search</a>
                            <a className="col" href="/partners">Partners</a>
                            <a className="col" href="/faq">FAQ</a>
                        {/* </p> */}
                        {/* </p>
                    </div>
                    <div className="col-4">
                        <p className="row"> */}
                        {/* <p className="row"> */}
                            <a className="col" href="/appendix">Appendix</a>
                            <a className="col" href="/accessibility">Accessibility Statement</a>
                            <a className="col" href="/privacy-policy">Privacy Policy</a>
                        {/* </p> */}
                    {/* </div> */}
                </div>

            </footer>
        )
    }


}

export default Footer;