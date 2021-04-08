import React from "react";
import PartnersTable from "./PartnersTable";

class Landing extends React.Component {
    componentDidMount() {
        document.title="EvictionSponge";
    }
    render() {
        return (
            <>
                <main>
                    <div className = "landing">
                        cool message
                    </div>
                    <div className="landingText">
                        <h1>
                            Easing the Process of<br/>Eviction Expungement
                        </h1>
                        <p>
                            Eviction Sponge is a software that helps organizations
                            <br/>
                            determine if an individual is elligable for eviction
                            <br/>
                            expungement.
                        </p>
                    </div>
                    <PartnersTable />
                </main>
            </>
        );
    }
}

export default Landing;