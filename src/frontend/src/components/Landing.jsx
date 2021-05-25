import React from "react";
import PartnersTableV2 from "./PartnersTableV2";
import "bootstrap/dist/css/bootstrap.css";

class Landing extends React.Component {

    componentDidMount() {
        document.title="EvictionSponge - Home";
    }

    render() {
        return (
            <>
                <main className="container-fluid mh57">
                    <h1 className="hidden">EvictionSponge Homepage</h1>
                    <div className="row justify-content-center py-4 landing">
                        cool message
                    </div>
                    <div className="row justify-content-center align-items-center">
                        <h2 className="col-md-4">
                            Easing the Process of Eviction Expungement
                        </h2>
                        <p className= "col-md-4">
                            Eviction Sponge is a software that helps organizations
                            determine if an individual is elligable for eviction
                            expungement.
                        </p>
                    </div>
                    <secion className="row">
                        <PartnersTableV2 />
                    </secion>
                </main>
            </>
        );
    }
}

export default Landing;