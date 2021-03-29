import React from "react";
import {Disclosure, DisclosureButton, DisclosurePanel,} from "@reach/disclosure";

/*
contains the PartnersTable component which arranges partners in a table
based of the PartnersTable from Record Sponge:
https://github.com/codeforpdx/recordexpungPDX/blob/master/src/frontend/src/components/PartnerTable/index.tsx
*/

class PartnersTable extends React.Component{
    constructor(props){
        super(props);
        this.state = {active: -1,};
    }

    render(){
        let partnerData = [
            {
                name: "Broseph Co.",
                area: "Northeast Portland",
                locations: "Multnomah County",
                incomeRestrictions: "None",
                analysisCost: "Free",
                paperWorkCost: "Free",
                courtFees: "Not Included",
                feeInfo: "The majority of court fees are subject to waiver",
                contacts: [
                    "Broseidon",
                    "Bro@Broseph.com",
                ],
                website: "https://www.youtube.com/watch?v=LJdKdITUyLM"
            },
            {
                name: "Fake Company",
                area: "Southeast Portland",
                locations: "Multnomah County",
                incomeRestrictions: "Must use Monopoly money",
                analysisCost: "$69",
                paperWorkCost: "$4.20",
                courtFees: "Three easy purchases of $9.99",
                feeInfo: "noice",
                contacts: [
                    "Arbys",
                    "wehavethemeats@arbys.com",
                ],
                website: "https://www.youtube.com/watch?v=0yGSQOWEXRo"
            },
        ]

        let partners;

        const toggleOpen = (order) => {
            this.setState({active: order === this.state.active ? -1 : order});
        };

        partners = partnerData.map((partner, index) => (
            <li>
                <Disclosure
                    open={index === this.state.active}
                    id={index}
                    onChange={() => toggleOpen(index)}
                >
                    <DisclosureButton className = "dbtnStyle">
                        <span className = "dbtnText">{partner.name}</span>
                        <span>{partner.area}</span>
                        <span>
                            {index === this.state.active ? (
                                <span aria-hidden = "true"></span>
                            ) : (
                                <span aria-hidden = "true"></span>
                            )}
                        </span>
                    </DisclosureButton>
                    <DisclosurePanel>
                        <div>
                            <ul>
                                <li>
                                    <span>{"Locations "}</span>
                                    <span>{partner.locations}</span>
                                </li>
                                <li>
                                    <span>{"Income Restrictions "}</span>
                                    <span>{partner.incomeRestrictions}</span>
                                </li>
                                <li>
                                    <span>{"Analysis Cost "}</span>
                                    <span>{partner.analysisCost}</span>
                                </li>
                                <li>
                                    <span>{"Court Fees "}</span>
                                    <span>{partner.courtFees}</span>
                                </li>
                            </ul>
                            <p>
                                <span>{partner.feeInfo}</span>
                            </p>
                            <hr/>
                            <p>{"Contact: "}</p>
                            <ul>
                                {partner.contacts.map((contact, index) => (
                                    <li>{contact}</li>
                                ))}
                            </ul>
                            <a href={partner.website}>
                                {partner.website}
                            </a>
                        </div>
                    </DisclosurePanel>
                </Disclosure>
            </li>
        ));
        return (
            <div className = "partnerTableBorder">
                <div className = "partnerTable">
                    <div>
                        <h3>Partners</h3>
                    </div>
                    <ul>{partners}</ul>
                </div>
            </div>
        );
    }
}

export default PartnersTable;