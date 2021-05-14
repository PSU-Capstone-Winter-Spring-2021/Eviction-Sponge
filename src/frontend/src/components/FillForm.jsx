import React from 'react';
import axios from 'axios';
import InvalidInputs from "./InvalidInputs";
import fileDownload from "js-file-download";

import 'bootstrap/dist/css/bootstrap.css';


// const testProps = {
//     county_name: 'Clark',
//     case_number: '11001001',
//     case_name: 'Charles Cheese v Caesar Jr',
//     date_of_judgment: '6/26/11',

//     plaintiff_line1: 'Charles Cheese',
//     plaintiff_line2: 'Nolan Bushnell',

//     defendant_line1: 'Caesar Jr',
//     defendant_line2: 'Ilitch Holdings',
//     defendant_line3: '',
//     defendant_line4: '',

//     def_full_name: 'Caesar Jr'
// }

class FillForm extends React.Component {
    constructor(props) {
        super(props);
        // this.props = testProps
        this.state = {
            county_name: this.props.location.state.county_name || '',
            case_number: this.props.location.state.case_number || '',
            case_name: this.props.location.state.case_name || '',
            date_of_judgment: this.props.location.state.date_of_judgement || '',
            plaintiff_line1: this.props.plaintiff_line1 || '',
            plaintiff_line2: this.props.plaintiff_line2 || '',

            defendant_line1: this.props.defendant_line1 || '',
            defendant_line2: this.props.defendant_line2 || '',
            defendant_line3: this.props.defendant_line3 || '',
            defendant_line4: this.props.defendant_line4 || '',

            def_full_name: this.props.def_full_name || '',
            def_mailing_address: '',
            def_city: '',
            def_state: '',
            def_zip: '',
            phone_number: '',

            plaintiff_mailing_address: '',
            plaintiff_city: '',
            plaintiff_state: '',
            plaintiff_zip: '',

            dismissal: false,
            restitution: false,
            money: false,
            judgment_date: false,
            stipulation: false,
            terms: false,

            invalid_defendant_zip_code: false,
            invalid_plaintiff_zip_code: false,
            invalid_phone: false
        }
        // this.getNames();
    }
    
    // Don't know that this will be needed
    // getNames() {
    //     let defendantFlag = false;
    //     let plaintiffs = [];
    //     let defendants = [];
    //     let names = this.props.location.state.case_name.split(" ");
    //     for(let i = 0; i < names.length; i++) {
    //         console.log("current string:" + names[i])
    //         if( names[i].toLowerCase() === "vs" || names[i].toLowerCase() === "vs.") {
    //             defendantFlag = true;
    //         }
    //         else if(defendantFlag) {
    //             defendants.push(names[i] + " ")
    //         }
    //         else {
    //             plaintiffs.push(names[i] + " ")
    //         }
    //     }
    //     this.setState({
    //         plaintiff_line1: plaintiffs.join(' '),
    //         defendant_line1: defendants.join(' '),
    //     })
    //     console.log("Defendants: " + defendants.join(' '));
    //     console.log("Plaintiffs: " + plaintiffs.join(' '));
    // }

    phoneNumberPattern = new RegExp('.*[0-9].*');
    zipCodePattern = new RegExp('[0-9][0-9][0-9][0-9][0-9].*');

    validateForm = () => {
        const phoneNumberMatch = this.phoneNumberPattern.exec(this.state.phone_number);
        const defendantZipCodeMatch = this.zipCodePattern.exec(this.state.def_zip);
        const plaintiffZipCodeMatch = this.zipCodePattern.exec(this.state.plaintiff_zip);
        return new Promise((resolve) => {
            this.setState(
                {
                    invalid_defendant_zip_code: this.state.def_zip.length > 0 && !defendantZipCodeMatch,
                    invalid_plaintiff_zip_code: this.state.plaintiff_zip.length > 0 && !plaintiffZipCodeMatch,
                    invalid_phone: this.state.phone_number.length > 0 && !phoneNumberMatch,
                },
                resolve
            );
        });
    };

    handleChange = ({ target }) =>
        this.setState({ [target.id]: target.value });

    handleToggle = ({ target }) =>
        this.setState(s => ({ ...s, [target.name]: !s[target.name] }));

    handleSubmit = (e) => {
        e.preventDefault();
        this.validateForm().then(() => {
            if (
                !this.state.invalidZipCode &&
                !this.state.invalid_phone &&
                !this.state.invalidBirthDate
            ) {
                const formData = toPdfFormFormat(this.state);
                axios(`/pdf`, {
                    method: 'POST',
                    responseType: 'blob',
                    data: formData
                }).then(response => {
                    const filename = response.headers["content-disposition"]
                        .split("filename=")[1]
                        .split(" ")[0];
                    const file = new Blob(
                        [response.data],
                        { type: 'application/pdf' });

                    fileDownload(file, filename);
                }).catch(error => {
                    console.log(error);
                });
            }
        });
    };

    render() {
        return (
            <main className="container">
                <h2 className="text-left">Generate Expungement Form</h2>
                <p className="text-left">
                    This will fill and download the required paperwork form as a PDF
                    file for the eviction record that is eligible for expungement.
                </p>

                <p className="text-left">
                    On this page, you may optionally provide the person's name,
                    address, and other information and it will be used to populate
                    the form. It is not required if you would prefer to fill out
                    the information later. We do not save any of this
                    information.
                </p>

                <p className="text-left">
                    Please read the complete instructions in the
                    {" "}<a href="/manual">Manual</a>{" "}
                    for filing the required form for expungement. After downloading
                    the PDF, review their contents to verify that all the required
                    information is present and correct.
                </p>
                <hr />
                <form onSubmit={this.handleSubmit} noValidate={true}>
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg text-left">
                            Case Information
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="county_name">
                                County Name
                            </label>
                            <input
                                className="col-sm form-control"
                                id="county_name"
                                name="county_name"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.county_name}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="case_number">
                                Case Number
                            </label>
                            <input
                                className="col-sm form-control"
                                id="case_number"
                                name="case_number"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.case_number}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="case_name">
                                Case Name
                            </label>
                            <input
                                className="col-sm form-control"
                                id="case_name"
                                name="case_name"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.case_name}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="date_of_judgment">
                                Date of judgment
                            </label>
                            <input
                                className="col-sm form-control"
                                id="date_of_judgment"
                                name="date_of_judgment"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.date_of_judgment}
                            />
                        </div>
                    </fieldset>
                    <hr />
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg text-left">
                            Plaintiff (Landlord or Agent)
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_line1">
                                Plaintiff 1
                            </label>
                            <input
                                className="col-sm form-control"
                                id="plaintiff_line1"
                                name="plaintiff_line1"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_line1}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_line2">
                                Plaintiff 2
                            </label>
                            <input
                                className="col-sm form-control"
                                id="plaintiff_line2"
                                name="plaintiff_line2"
                                type="text"
                                required={false}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_line2}
                            />
                        </div>
                    </fieldset>
                    <hr />
                    <fieldset className="form-group">
                        <legend className="col-form-label col-form-label-lg text-left">
                            Defendant (Tenant or Occupant)
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="defendant_line1">
                                Defendant 1
                            </label>
                            <input
                                className="col-sm form-control"
                                id="defendant_line1"
                                name="defendant_line1"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.defendant_line1}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="defendant_line2">
                                Defendant 2
                            </label>
                            <input
                                className="col-sm form-control"
                                id="defendant_line2"
                                name="defendant_line2"
                                type="text"
                                required={false}
                                onChange={this.handleChange}
                                value={this.state.defendant_line2}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="defendant_line3">
                                Defendant 3
                            </label>
                            <input
                                className="col-sm form-control"
                                id="defendant_line3"
                                name="defendant_line3"
                                type="text"
                                required={false}
                                onChange={this.handleChange}
                                value={this.state.defendant_line3}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="defendant_line4">
                                Defendant 4
                            </label>
                            <input
                                className="col-sm form-control"
                                id="defendant_line4"
                                name="defendant_line4"
                                type="text"
                                required={false}
                                onChange={this.handleChange}
                                value={this.state.defendant_line4}
                            />
                        </div>
                    </fieldset>
                    <hr />
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg text-left">
                            Declaration
                        </legend>

                        <div className="form-group text-left">
                            <div className="form-group form-check">
                                <input
                                    className="form-check-input"
                                    id="dismissal"
                                    name="dismissal"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.dismissal}
                                />
                                <label className="form-check-label" htmlFor="dismissal">
                                    Dismissal in my favor (I was not ordered to leave the property)
                                </label>
                            </div>
                            <div className="form-group form-check">
                                <input
                                    className="form-check-input"
                                    id="restitution"
                                    name="restitution"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.restitution}
                                />
                                <label className="form-check-label" htmlFor="restitution">
                                    Restitution in Plaintiff’s favor (I was ordered to leave the property)
                                </label>
                            </div>
                            <div className="form-group form-check ml-4">
                                <input
                                    className="form-check-input"
                                    id="money"
                                    name="money"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.money}
                                />
                                <label className="form-check-label" htmlFor="money">
                                    I have satisfied any money awards ordered in the judgment
                                </label>
                            </div>
                            <div className="form-group form-check ml-4">
                                <input
                                    className="form-check-input"
                                    id="judgment_date"
                                    name="judgment_date"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.judgment_date}
                                />
                                <label className="form-check-label" htmlFor="judgment_date">
                                    Judgment was entered on {this.state.date_of_judgment}, which is 5 or more years ago.
                                </label>
                            </div>

                            <div className="form-group form-check">
                                <input
                                    className="form-check-input"
                                    id="stipulation"
                                    name="stipulation"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.stipulation}
                                />
                                <label className="form-check-label" htmlFor="stipulation">
                                    Stipulation (agreement)
                                </label>
                            </div>
                            <div className="form-group form-check ml-4">
                                <input
                                    className="form-check-input"
                                    id="terms"
                                    name="terms"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.terms}
                                />
                                <label className="form-check-label" htmlFor="terms">
                                    I have satisfied all terms of the agreement and paid any money required
                                </label>
                            </div>
                        </div>

                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="def_full_name">
                                Full Name
                            </label>
                            <input
                                className="col-sm form-control"
                                id="def_full_name"
                                name="def_full_name"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.def_full_name}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="def_mailing_address">
                                Mailing Street Address
                            </label>
                            <input
                                className="col-sm form-control"
                                id="def_mailing_address"
                                name="def_mailing_address"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.def_mailing_address}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="def_city">
                                City
                            </label>
                            <input
                                className="col-sm form-control"
                                id="def_city"
                                name="def_city"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.def_city}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="def_state">
                                State
                            </label>
                            <input
                                className="col-sm form-control"
                                id="def_state"
                                name="def_state"
                                list="def_state"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.def_state}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="def_zip">
                                Zip Code
                            </label>
                            <input
                                className="col-sm form-control"
                                id="def_zip"
                                name="def_zip"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.def_zip}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="phone_number">
                                Phome Number
                            </label>
                            <input
                                className="col-sm form-control"
                                id="phone_number"
                                name="phone_number"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.phone_number}
                            />
                        </div>
                    </fieldset>
                    <hr />
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg text-left">
                            Plaintiff Mailing Address
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_mailing_address">
                                Street Address
                            </label>
                            <input
                                className="col-sm form-control"
                                id="plaintiff_mailing_address"
                                name="plaintiff_mailing_address"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_mailing_address}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_city">
                                City
                            </label>
                            <input
                                className="col-sm form-control"
                                id="plaintiff_city"
                                name="plaintiff_city"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_city}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_state">
                                State
                            </label>
                            <input
                                className="col-sm form-control"
                                id="plaintiff_state"
                                name="plaintiff_state"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_state}
                            />
                        </div>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label text-left" htmlFor="plaintiff_zip">
                                Zip Code
                            </label>


                            <input
                                className="col-sm form-control"
                                id="plaintiff_zip"
                                name="plaintiff_zip"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.plaintiff_zip}
                            />
                        </div>
                    </fieldset>
                    <div className="row">
                        <div className="col form-group">
                            <button type="submit" className="btn btn-primary m-2 float-right">
                                Download PDF
                            </button>
                        </div>
                    </div>
                </form>
                <div className="row">
                    <div className="col">
                        <div className="float-right">
                            <InvalidInputs
                                conditions={[
                                    this.state.invalid_defendant_zip_code,
                                    this.state.invalid_plaintiff_zip_code,
                                    this.state.invalid_phone,
                                ]}
                                contents={[
                                    <span>Zip code must lead with five digits</span>,
                                    <span>Zip code must lead with five digits</span>,
                                    <span>Phone number must contain a digit</span>,
                                ]}
                            />
                        </div>
                    </div>
                </div>
            </main>
        );
    }
}

const toPdfFormFormat = (s) => {
    const defCityStateZip = build_address({
        city: s.def_city,
        state: s.def_state,
        zip: s.def_zip
    })

    const plaintiffAddress = build_address({
        address: s.plaintiff_mailing_address,
        city: s.plaintiff_city,
        state: s.plaintiff_state,
        zip: s.plaintiff_zip
    })

    let pdfData = {
        ...s,
        'city_state_zip': defCityStateZip,
        'plaintiff_address': plaintiffAddress
    }

    delete pdfData['def_city']
    delete pdfData['def_state']
    delete pdfData['def_zip']
    delete pdfData['plaintiff_mailing_address']
    delete pdfData['plaintiff_city']
    delete pdfData['plaintiff_state']
    delete pdfData['plaintiff_zip']
    delete pdfData['invalid_defendant_zip_code']
    delete pdfData['invalid_plaintiff_zip_code']
    delete pdfData['invalid_phone']

    return pdfData
}

const build_address = ({ address = '', city = '', state = '', zip = '' }) => {
    const addressCityState = [address, city, state].filter(Boolean).join(', ');
    const addressCityStateZip = [addressCityState, zip].filter(Boolean).join(' ')
    return addressCityStateZip
}

export default FillForm;