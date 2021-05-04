import React from "react";
import "bootstrap/dist/css/bootstrap.css";

class FaqPage extends React.Component{
    componentDidMount(){
        document.title = "faq"
    };

    render(){
        return(
            <div className="container-fluid bg-light">
                <div
                className="container bg-light text-left"
                style={{maxWidth: "720px"}}
                >
                    <div className="row mb-4">
                        <h1 className="col font-weight-bold text-left">
                            FAQ
                        </h1>
                    </div>
                    <section className="row mb-4">
                        <p className="col">
                            Due to the complexity of the Oregon expungement laws, incorrect
                            information proliferates from State actors at all levels of the
                            justice system. <br/> Below are some common myths overheard in
                            courtrooms all over oregon
                        </p>
                    </section>
                </div>
                <section
                className="container bg-light"
                style={{maxWidth: "720px"}}
                >
                    <ol className="text-left">
                        <li className="container mb-4">
                            <p className="row font-weight-bold mb-3">
                                Myth: "This is a myth"
                            </p>
                            <p className="row font-weight-bold mb-3">
                                Fact 1: "This is a fact refuting that myth"
                            </p>
                            <p className="row mb-3">
                                details into why myth is false
                            </p>
                            <p className="row font-weight-bold mb-3">
                                Fact 2: "This is another fact refuting that myth"
                            </p>
                            <p className="row mb-3">
                                details into why myth is false
                            </p>
                        </li>
                        <li className="container mb-4">
                            <p className="row font-weight-bold mb-3">
                                Myth: "This is another myth"
                            </p>
                            <p className="row font-weight-bold mb-3">
                                Fact 1: "This is a fact refuting that myth"
                            </p>
                            <p className="row mb-3">
                                details into why myth is false
                            </p>
                            <p className="row font-weight-bold mb-3">
                                Fact 2: "This is another fact refuting that myth"
                            </p>
                            <p className="row mb-3">
                                details into why myth is false
                            </p>
                        </li>
                    </ol>
                </section>

            </div>
        );
    }
}

export default FaqPage;