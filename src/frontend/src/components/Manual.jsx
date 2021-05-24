import React from "react";
import "bootstrap/dist/css/bootstrap.css";

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
            <main className="container bg-light w-100 m-0 mw-100 px-0 pt-sm-3 mh57">
                <h1>EvictionSponge Manual</h1>
                <div className="row mx-0">
                    <nav className="col border d-xs-block d-sm-none">
                        <ul className="list-unstyled mb-0">
                        <li className="border-bottom">
                            <a href="#introduction">
                            Introduction
                            </a>
                        </li>
                        <li className="border-bottom">
                            <a href="#information">
                            General Information
                            </a>
                        </li>
                        <li className="border-bottom">
                            <a href="#howto">
                            How to Use EvictionSponge
                            </a>
                        </li>
                        <li className="border-bottom">
                            <a href="#assumption">
                            Assumption
                            </a>
                        </li>
                        <li className="border-bottom">
                            <a href="#formNotes">
                            Notes on Forms
                            </a>
                        </li>
                        </ul>
                     </nav>
                </div>
                <div className="row mx-0 justify-content-center">
                    <div className="col-sm-9 col-lg-6 text-left">
                        <section>
                            <h2 id="introduction">
                                Introduction
                            </h2>
                            <p className="">EvictionSponge is a web application used to facilitate the expungement process for evictions that occured in Oregon. It is built by a team of students at PSU for their capstone project and is based on the RecordSponge project by Code for PDX. The codebase is published under an open source MIT license.</p>
                            <p>This Manual explains how EvictionSponge is used and the process of expunging eviction records. </p>
                        </section>
                        <section className="">
                            <h2 id="information">General Info</h2>
                                <p>Having an eviction in your pase can make finding affordable housing more difficult. Oregon law allows for certain types of eviction records to be removed from public view, or "expunged." Expunged evictions should not show up during a background check and the tenant can answer housing applications as if they eviction had not occurred. EvictionSponge aims to make finding eligible expungements easy and accessible.</p>
                                <p>Please not that EvictionSponge can only be used to find eviction records for Oregon cases.</p>
                            <h3 className="h5">Eviction casese are eligible if they meet any of the following criteria:</h3>
                                <ul>
                                    <li>The case went to trial and the tenant won at trial</li>
                                    <li>The case resulted in a judgment, and the judgment is at least five years old, AND
                                        <li>The tenant doesn't owe any money that was included in the judgment</li>
                                    </li>
                                    <li>The case resulted in a negotiated agreement and the tenant has complied with any terms in court agreements</li>
                                </ul>
                            <p>Please contact <a href="mailto:michael@qiu-qiulaw.com">michael@qiu-qiulaw.com</a> if you would like to set up EvictionSponge at your organization.</p>
                        </section>
                        <section>
                            <h2 id="howto">How to Use EvictionSponge</h2>
                                <h3>Overview</h3>
                                    <ol>
                                        <li><a href="oeci-login">Log in</a>
                                            <ul>
                                                <li>You will need an Oregon eCourt Case Information (OECI) account to search for civil records. You can purchase a subscription <a href="https://www.courts.oregon.gov/services/online/pages/ojcin.aspx">here</a>.</li>
                                            </ul>
                                        </li>
                                        <li><a href="/record-search">Search records</a> by First and Last name</li>
                                        <li>For eligible records of eviction judgments, <a href="#assumption">Assumption 1</a> is met</li>
                                        <li>Confirm positive search results with Michael: <a href="mailto:michael@qiu-qiulaw.com">michael@qiu-qiulaw.com</a></li>
                                        <li>Complete forms (See note below on Forms)</li>
                                        <li>Instruct clients to file paperwork in appropriate courts</li>
                                    </ol>
                            <h2 id="assumption">Assumption (Eviction judgment filing fees paid)</h2>
                            <p>Eviction judgments are eligible after five years IF a person pays off the landlord’s filing fees associated with the case. This is not the same thing as back-rent. It is usually an amount less than $300, which you can find by going to the eCourts link for that case.</p>
                            <p className="font-weight-bold">Therefore, if a client has an eviction judgment, check with the tenant that the tenant does not owe the filing fees or they pay it before filing the application.</p>
                            <p>EvictionSponge has no record of payments, so charges marked as eligible do not take whether any payments were made on the filing fees. </p>
                                {/* EvictionSponge does it’s best to find the correct monetary value owed, but it is possible that it is incorrect in some cases, please verify the total amount owed before instructing the client to make any payments.</p> */}
                            <h2 id="formNotes">Notes on Forms</h2>
                            <p>EvictionSponge makes filling out the pro se eviction expungement form easier through its intuitive interface. Simply click on the link next to eligible cases and fill out as many boxes as you can.</p>
                            <p>Make sure to fill out the Plaintiff mailing address with the address of the Plaintiff provided in eCourts. If none is provided, you may be able to find the Plaintiff’s mailing address through the Secretary of State’s website.</p>
                        </section>
                    </div>
                    <nav className="subnav col-sm-3 border d-none d-sm-block sticky-top h-25">
                        <ul className="list-unstyled text-left">
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
                            <a href="#howto">
                            How to Use EvictionSponge
                            </a>
                        </li>
                        <li>
                            <a href="#assumption">
                            Assumption
                            </a>
                        </li>
                        <li>
                            <a href="#formNotes">
                            Notes on Forms
                            </a>
                        </li>
                        </ul>
                    </nav>
                </div>
            </main>
        )
    }
}

export default Manual;