                                import React from "react";


class Footer extends React.Component {

    /*constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
    };*/

    // HTML(?) for the component
    render() {
        return (
            <footer>
                <p><a href="#">Home</a></p>
                <p><a href="#">About Us</a></p>
                <p><a href="#">Partners</a></p>
                <p><a href="#">Manual</a></p>
                <p><a href="#">Search</a></p>
                <p><a href="#">Etc</a></p>
            </footer>
        )
    }


}

export default Footer;