import React from "react";

class Appendix extends React.Component {

    componentDidMount(){
        document.title = "Appendix - EvictionSponge";
    }

    render() {
        return (
            <main className="bg-light mh57">
                <section className="container text-left">
                    <div className="w-75">
                        <h2 className="pb-3 pt-4">Appendix</h2>
                        <p className="font-weight-bold">Form to file for expungement</p>
                        <p>
                            EvictionSponge supports automatic form-filling for the form
                            listed below. You can also fill out the form manually if
                            preferred. <a href="/manual#file">Learn more in the Manual</a>.
                        </p>
                        <hr />
                        <div className="my-3 pb-5">
                            <p>Oregon</p>
                            <a
                                className="px-3"
                                href="https://www.courts.oregon.gov/forms/Documents/FED-Motion-SetAside-2020-01-01.pdf"
                            >
                                <small>FED Motion SetAside <span className="badge badge-secondary">PDF</span></small>
                            </a>
                        </div>
                    </div>
                </section>
            </main>
        )
    }
}

export default Appendix;