import React from "react";
import PartnersTableV2 from "./PartnersTableV2";
import "bootstrap/dist/css/bootstrap.css";

class Landing extends React.Component {
    componentDidMount() {
        document.title="EvictionSponge";
    }
    render() {
        return (
            <>
                <main className="container-fluid">
                    <div className="container-fluid py-4 mb-5 landing">
                        cool message
                    </div>
                    <div className="row justify-content-center align-items-center">
                        <h1 className="col-md-3">
                            Easing the Process of Eviction Expungement
                        </h1>
                        <p className= "col-md-3">
                            Eviction Sponge is a software that helps organizations
                            determine if an individual is elligable for eviction
                            expungement.
                        </p>
                    </div>
                    <PartnersTableV2/>
                </main>
            </>
        );
    }
}

export default Landing;