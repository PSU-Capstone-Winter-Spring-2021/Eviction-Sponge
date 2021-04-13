import React from 'react';
import axios from 'axios';
import InvalidInputs from "./InvalidInputs";

import 'bootstrap/dist/css/bootstrap.css';


// const testProps = {
//     county_name: 'Clark',
//     case_number: '11001001',
//     case_name: 'Charles Cheese v Caesar Jr',
//     date_of_judgement: '6/26/11',

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
            county_name: this.props.county_name || '',
            case_number: this.props.case_number || '',
            case_name: this.props.case_name || '',
            date_of_judgement: this.props.date_of_judgement || '',

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
            judgement: false,
            stipulation: false,
            terms: false,

            invalid_defendant_zip_code: false,
            invalid_plaintiff_zip_code: false,
            invalid_phone: false
        }
    }

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
                console.log(formData)
                axios.post('/pdf', formData)
                    .then(response => console.log(response.json()));
            }
        });
    };

    render() {
        return (
            <main className="container">
                <form onSubmit={this.handleSubmit} noValidate={true}>
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg">
                            Case Information
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label" htmlFor="county_name">
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
                            <label className="col-sm-3 col-form-label" htmlFor="case_number">
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
                            <label className="col-sm-3 col-form-label" htmlFor="case_name">
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
                            <label className="col-sm-3 col-form-label" htmlFor="date_of_judgement">
                                Date of judgement
                            </label>
                            <input
                                className="col-sm form-control"
                                id="date_of_judgement"
                                name="date_of_judgement"
                                type="text"
                                required={true}
                                onChange={this.handleChange}
                                value={this.state.date_of_judgement}
                            />
                        </div>
                    </fieldset>
                    <hr />
                    <fieldset>
                        <legend className="col-form-label col-form-label-lg">
                            Plaintiff (Landlord or Agent)
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_line1">
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
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_line2">
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
                        <legend className="col-form-label col-form-label-lg">
                            Defendant (Tenant or Occupant)
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label" htmlFor="defendant_line1">
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
                            <label className="col-sm-3 col-form-label" htmlFor="defendant_line2">
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
                            <label className="col-sm-3 col-form-label" htmlFor="defendant_line3">
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
                            <label className="col-sm-3 col-form-label" htmlFor="defendant_line4">
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
                        <legend className="col-form-label col-form-label-lg">
                            Declaration
                        </legend>
                        <div className="form-group">
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
                                    dismissal in my favor (I was not ordered to leave the property)
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
                                    restitution in Plaintiff’s favor (I was ordered to leave the property)
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
                                    disabled={!this.state.restitution}
                                />
                                <label className="form-check-label" htmlFor="money">
                                    I have satisfied any money awards ordered in the judgment
                                </label>
                            </div>
                            <div className="form-group form-check ml-4">
                                <input
                                    className="form-check-input"
                                    id="judgement"
                                    name="judgement"
                                    type="checkbox"
                                    required={false}
                                    onChange={this.handleToggle}
                                    value={this.state.judgement}
                                    disabled={!this.state.restitution}
                                />
                                <label className="form-check-label" htmlFor="judgement">
                                    Judgment was entered on {this.state.date_of_judgement} which is more than 5 years before this Motion was filed
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
                                    stipulation (agreement)
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
                                    disabled={!this.state.stipulation}
                                />
                                <label className="form-check-label" htmlFor="terms">
                                    I have satisfied all terms of the agreement and paid any money required
                                </label>
                            </div>
                        </div>

                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label" htmlFor="def_full_name">
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
                            <label className="col-sm-3 col-form-label" htmlFor="def_mailing_address">
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
                            <label className="col-sm-3 col-form-label" htmlFor="def_city">
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
                            <label className="col-sm-3 col-form-label" htmlFor="def_state">
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
                            <label className="col-sm-3 col-form-label" htmlFor="def_zip">
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
                            <label className="col-sm-3 col-form-label" htmlFor="phone_number">
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
                        <legend className="col-form-label col-form-label-lg">
                            Plaintiff Mailing Address
                        </legend>
                        <div className="form-group row">
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_mailing_address">
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
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_city">
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
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_state">
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
                            <label className="col-sm-3 col-form-label" htmlFor="plaintiff_zip">
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
    const defCityStateZip = `${s.def_city}, ${s.def_state} ${s.def_zip}`
    const plaintiffAddress = `${s.plaintiff_mailing_address}, ${s.plaintiff_city}, ${s.plaintiff_state} ${s.plaintiff_zip}`

    const newProps = { 'city_state_zip': defCityStateZip, 'plaintiff_address': plaintiffAddress }
    let newState = { ...s, ...newProps }

    delete newState['def_city']
    delete newState['def_state']
    delete newState['def_zip']
    delete newState['plaintiff_mailing_address']
    delete newState['plaintiff_city']
    delete newState['plaintiff_state']
    delete newState['plaintiff_zip']

    return newState

}

export default FillForm;