import React from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

export default class PartnersPage extends React.Component{

    componentDidMount(){
        document.title="Partner with us - EvictionSponge";
    };

    state = {
        email: "",
        invalidEmail: false,
    };

    validateEmail = (email) => {
        var pattern = new RegExp(/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w+)+$/);
        return pattern.test(email);
    };

    handleSubmit = (e) => {
        if(!this.validateEmail(this.state.email)){
            e.preventDefault();
            this.setState({invalidEmail: true});
        }
        else{
            this.setState({invalidEmail: false});
        }
        console.log(this.state.invalidEmail);
    };

    const
    divStyle = {
    marginLeft: '10px',
    };

    render(){
        return(
        <>
            <div className="container-fluid bg-light pb-4 pt-3">
                <div className="container bg-light text-left" style={{maxWidth: "720px"}}>
                    <h1 className="hidden">Partners Interest Page</h1>
                    <div className="row mb-4">
                        <h2 className="col font-weight-bold text-left">
                            Interested in becoming a partner?
                        </h2>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            EvictionSponge is made for organizations looking for help in determining
                            whether or not their clients are eligable for eviction expungement. We
                            provide the software, while organizations provide the clients and
                            expungement service.
                        </p>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            We are looking to partner with organizations in contact with people who
                            have been evicted. If you would like to learn more, please fill out the
                            contact form below.
                        </p>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            You will need an Oregon eCourt Case Information (OECI) account to search
                            for eviction records with EvictionSponge, otherwise the service is free.
                        </p>
                    </div>
                    <p> Are you interested in becoming a partner for EvictionSponge or want to learn more about the software?</p>
                    <p className="text-center">If so, click the button below!</p>
                    <p className="text-center">
                        <a href="https://docs.google.com/forms/u/1/d/1nD3nfYfKj9PSFXESRcME0ufSKhmmXFGTdhLBhRdhErk/edit?usp=drive_web"
                           className="btn btn-info button" role="button">Partner Interest</a>
                    </p>
                </div>
            </div>
        </>


        );
    }
}