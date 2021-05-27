import React from "react";
import PartnersTableV2 from "./PartnersTableV2";

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
                        <p>
                        EvictionSponge was made possible by a group of students at <br/> 
                        Portland State University for their senior capstone project.<br/>
                            <a href="/about" style={{color:"white"}}>Come meet the team
                                <svg xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                class="bi bi-arrow-right"
                                viewBox="0 0 16 16">
                                    <path fill-rule="evenodd"
                                    d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                                </svg>
                            </a>
                        </p>
                    </div>
                    <div className="row justify-content-center align-items-center">
                        <h2 className="col-md-4">
                            Easing the Process of Eviction Expungement
                        </h2>
                        <p className= "col-md-4">
                            Eviction Sponge is a software that helps organizations
                            determine if an individual is eligible for eviction
                            expungement.
                        </p>
                    </div>
                    <section className="row">
                        <PartnersTableV2 />
                    </section>
                </main>
            </>
        );
    }
}

export default Landing;