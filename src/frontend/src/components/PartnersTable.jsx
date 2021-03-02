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
            <li className="bt bw2 b--lightest-blue1">
                <Disclosure
                    open={index === this.state.active}
                    id={index}
                    onChange={() => toggleOpen(index)}
                >
                    <DisclosureButton className = "flex-ns w-100 relative navy hover-blue pv3 ph3">
                        <span className = "w-70 db pr3 mb2 mb0-ns">{partner.name + " "}</span>
                        <span className = "w-30 pr3">{partner.area}</span>
                        <span classname = "absolute top-0 right-0 pt3 ph3">
                            {index == this.state.active ? (
                                <span aria-hidden = "true" className = "fas fa-angle-up"></span>
                            ) : (
                                <span aria-hidden = "true" className = "fas fa-angle-down"></span>
                            )}
                        </span>
                    </DisclosureButton>
                    <DisclosurePanel>
                        <div classname = "b1 bw2 f5 b--blue pv3 ph3 mb3 ml3">
                            <ul className = "flex-ns mb3">
                                <li className = "flex-ns mb3">
                                    <span className = "w10rem db fw6 mr3">{"Locations "}</span>
                                    <span>{partner.locations}</span>
                                </li>
                                <li className = "flex-ns mb3">
                                    <span className = "w10rem db fw6 mr3">{"Income Restrictions "}</span>
                                    <span>{partner.incomeRestrictions}</span>
                                </li>
                                <li className = "flex-ns mb3">
                                    <span className = "w10rem db fw6 mr3">{"Analysis Cost "}</span>
                                    <span>{partner.analysisCost}</span>
                                </li>
                                <li className = "flex-ns mb3">
                                    <span className = "w10rem db fw6 mr3">{"Court Fees "}</span>
                                    <span>{partner.courtFees}</span>
                                </li>
                            </ul>
                            <p className = "mw6 lh-copy mb3">
                                <span>{partner.feeInfo}</span>
                            </p>
                            <hr className = "bt b--black-05 mb3" />
                            <p className = "fw6 mb3">{"Contact: "}</p>
                            <ul classname = "list mb3">
                                {partner.contacts.map((contact, index) => (
                                    <li className = "mb3">{contact}</li>
                                ))}
                            </ul>
                            <a href={partner.website} className = "link hover-blue bb">
                                {partner.website}
                            </a>
                        </div>
                    </DisclosurePanel>
                </Disclosure>
            </li>
        ));
        return (
            <div className = "ba bw3 br3 b--lightest-blue1 bg-white mb4">
                <div className="flex items-center justify-between">
                    <h3 className = "f3 fw9 pv4 ph3">Partners</h3>
                </div>
                <ul className = "list">{partners}</ul>
            </div>
        );
    }
}

export default PartnersTable;