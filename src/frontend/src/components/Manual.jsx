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

    // HTML for the component
    render() {
        return (
        <>
            <nav>
            <ul className="list">
              <li>
                <a href="#introduction">
                  Introduction
                </a>
              </li>
              <li>
                <a href="#information">
                  General Information
                </a>
              </li>
              <li>
                <a href="#overview">
                  Use EvictionSponge
                </a>
              </li>
              <li>
                <a href="#assumptions">
                  Assumptions
                </a>
              </li>
              <li>
                <a href="#search">
                  Search
                </a>
              </li>
              <li>
                <a href="#file">
                  File for Eviction Expungement
                </a>
              </li>
            </ul>
            </nav>
            <a name="introduction">
                <p>
                    Introduction
                </p>
            </a>
            <a name="information">
                <p>
                    General Information
                </p>
            </a>
            <a name="overview">
                <p>
                    Use EvictionSponge
                </p>
            </a>
            <a name="assumptions">
                <p>
                    Assumptions
                </p>
            </a>
            <a name="search">
                <p>
                    Search
                </p>
            </a>
            <a name="file">
                <p>
                    File for Eviction Expungement
                </p>
            </a>
        </>

        )
    }
}

export default Manual;