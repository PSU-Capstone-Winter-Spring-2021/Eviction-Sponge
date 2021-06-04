import React from "react";
import axios from 'axios';
import Accordion from "react-bootstrap/Accordion";
import Card from "react-bootstrap/Card";

class PartnersTableV2 extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            partnerData: [],
            dataLoaded: false
        };
    }

    componentDidMount() {
        axios.get('/partners-table')
            .then(({ data }) => {
                if(data.length > 0){
                    this.setState({
                        partnerData: data,
                        dataLoaded: true
                    });
                }
            }, reason =>{
                console.log("Internal Server Error, can't retrieve data")
                this.setState({
                    dataLoaded: false
                });
            })
    }

    render() {
        let partners = this.state.partnerData.map((partner, index) => (
            <Card className="row bg-light" key={partner.id}>
                <Accordion.Toggle
                as={Card.Header}
                eventKey={partner.id}
                className="row bg-light align-items-center">
                    <span className="col-6 text-left">{partner.name}</span>
                    <span className="col-6 text-right">{partner.area}</span>
                </Accordion.Toggle>
                <Accordion.Collapse
                eventKey={partner.id}
                className="row">
                    <Card.Body>
                        <ul>
                            <li className="row mb-2">
                                <span className="col-4 font-weight-bold text-left">{"Locations: "}</span>
                                <span className="col text-left">{partner.locations}</span>
                            </li>
                            <li className="row mb-2">
                                <span className="col-4 font-weight-bold text-left">{"Income Restrictions: "}</span>
                                <span className="col text-left">{partner.incomeRestrictions}</span>
                            </li>
                            <li className="row mb-2">
                                <span className="col-4 font-weight-bold text-left">{"Analysis Cost: "}</span>
                                <span className="col text-left">{partner.analysisCost}</span>
                            </li>
                            <li className="row mb-2">
                                <span className="col-4 font-weight-bold text-left">{"Court Fees: "}</span>
                                <span className="col text-left">{partner.courtFees}</span>
                            </li>
                            <li className="row mb-2">
                                <span className="col text-left">{partner.feeInfo}</span>
                            </li>
                        </ul>
                        <hr/>
                        <ul>
                            <li className="row mb-2">
                                <span className="col font-weight-bold text-left">{"Contact: "}</span>
                            </li>
                            {partner.contacts.map((contact, index) => (
                                <li key={partner.id + index.toString()} className="row mb-2">
                                    <span className="col text-left">{contact}</span>
                                </li>
                            ))}
                            <a href={partner.website}
                            className="row mb-2">
                                <span className="col text-left">{partner.website}</span>
                            </a>
                        </ul>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        ));
        if(this.state.dataLoaded){
        return(
            <div
            className="container-fluid py-5"
            style={{backgroundColor:"green"}}>
                <Accordion
                    className="container-md bg-white rounded pt-2"
                    style={{maxWidth: "720px"}}>
                    <div className="row">
                        <h2 className="col text-left">Partners</h2>
                    </div>
                    {partners}
                </Accordion>
            </div>
        );
        }
        else{
            return(
                <div
                className="container-fluid py-5"
                style={{backgroundColor:"green"}}>
                    <div
                    className = "container-md bg-white rounded pt-2"
                    style={{maxWidth: "720px"}}>
                        <div className="row">
                            <h2 className="col">We're looking for Partners!</h2>
                        </div>
                        <div className="row">
                            <p className ="col">
                                If you're interested in working with EvictionSponge and putting
                                our services in the hands of more people, please let us know by
                                contacting us - We'd love to work with you! <br/>
                                <a href="/partners">Contact Us
                                <svg xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fillRule="currentColor"
                                className="bi bi-arrow-right"
                                viewBox="0 0 16 16">
                                    <path fillRule="evenodd"
                                    d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                                </svg>
                                </a>
                            </p>
                        </div>
                    </div>
                </div>
            )
        }
    }
}

export default PartnersTableV2;