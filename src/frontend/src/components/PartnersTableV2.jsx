import React from "react";
import Accordion from "react-bootstrap/Accordion";
import Card from "react-bootstrap/Card";
import partnerData from "../data/partnerData.json";
import "bootstrap/dist/css/bootstrap.css";

class PartnersTableV2 extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        let partners = partnerData.map((partner, index) => (
            <Card className="row bg-light">
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
                            <p className="row mb-2">
                                <span className="col text-left">{partner.feeInfo}</span>
                            </p>
                        </ul>
                        <hr/>
                        <ul>
                            <p className="row mb-2">
                                <span className="col font-weight-bold text-left">{"Contact: "}</span>
                            </p>
                            {partner.contacts.map((contact, index) => (
                                <li className="row mb-2">
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
        return(
            <div 
                className="container-fluid py-5 my-4"
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
}

export default PartnersTableV2;