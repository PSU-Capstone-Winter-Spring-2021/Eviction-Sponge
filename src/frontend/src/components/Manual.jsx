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
            <main className="container bg-light w-100 m-0 mw-100 px-0 pt-3">
                <div className="row mx-0">
                    <nav className="col border d-xs-block d-sm-none">
                        <ul className="list-unstyled">
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
                            <a href="#assumption1">
                            Assumption 1
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
                            <h2>General Info</h2>
                                <p>Having an eviction on your record can make finding affordable housing difficult. An eviction expungement may help remedy this for people who are in this situation because an expungement means that the eviction record is erased and the court treats the eviction as if it never happened. Evictions should not show up during a background check and the tenant can answer “no” regarding evictions on future applications. EvictionSponge aims to make finding eligible expungements easy and accessible.</p>
                                <p>Eviction expungement in Oregon was introduced in January, 2021. EvictionSponge can only find eviction records for Oregon cases.</p>
                            <h3 className="h5">There are a few requirements for an eviction to be eligible for expungement:</h3>
                                <ul>
                                    <li>The tenant won and the eviction was dismissed</li>
                                    <p className="font-weight-bold my-1">or</p>
                                    <li>The final court judgement is at least five years old, and</li>
                                    <li>The tenant doesn't owe any money that was included in the judgement, and</li>
                                    <li>The tenant has complied with any terms in court agreements</li>
                                </ul>
                            <p>We still need partners to administer EvictionSponge. Please contact <a href="mailto:michael@qiu-qiulaw.com">michael@qiu-qiulaw.com</a> if you would like to set up EvictionSponge at your organization.</p>
                        </section>
                        <section>
                            <h2>How to Use EvictionSponge</h2>
                                <h3>Overview</h3>
                                    <ol>
                                        <li>Log in
                                            <ul>
                                                <li>You will need an Oregon eCourt Case Information (OECI) account to search for civil records. You can purchase a subscription here.</li>
                                            </ul>
                                        </li>
                                        <li><a href="#">Search records</a> by First and Last name</li>
                                        <li>Assure that <a href="#assumption1">Assumption 1</a> is met</li>
                                        <li>Confirm positive search results with Michael: <a href="mailto:michael@qiu-qiulaw.com">michael@qiu-qiulaw.com</a></li>
                                        <li>Complete forms</li>
                                        <li>Instruct clients to file paperwork in appropriate courts</li>
                                    </ol>
                            <h2 id="assumption1">Assumption 1</h2>
                            <p className="font-weight-bold">The tenant does not owe money to the landlord on the case or they pay it before filing the application.</p>
                            <p>This assumption is redundant with an assumption needed for correct analysis. EvictionSponge has no record of payments so charges marked as eligible do not take into account any payments made. EvictionSponge does it’s best to find the correct monetary value owed, but it is possible that it is incorrect in some cases, please verify the total amount owed before instructing the client to make any payments.</p>
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
                            <a href="#assumption1">
                            Assumption 1
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
                </div>
            </main>
        )
    }
}

export default Manual;