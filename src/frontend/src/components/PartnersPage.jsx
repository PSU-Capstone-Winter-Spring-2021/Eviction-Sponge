import React from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.css";

export default class PartnersPage extends React.Component{
    componentDidMount(){
        document.title="PartnersPage";
    }

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

    render(){
        return(
            <div className="container-fluid bg-light">
                <div
                className="container bg-light text-left"
                style={{maxWidth: "720px"}}
                >
                    <div className="row mb-4">
                        <h2 className="col font-weight-bold text-left">
                            'Sah Dude
                        </h2>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            EvictionSponge is made for organizations looking for help in determining
                            whether or not their clients are elligable for eviction expungement. We
                            provide the software, while organizations provide the clients and
                            expungement service.
                        </p>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            We are looking to partner with organizations in contact with people who
                            have been evicted. If you would like to learn more, please fill out the
                            contact form bellow.
                        </p>
                    </div>
                    <div className="row mb-4">
                        <p className="col">
                            You will need an Oregon eCourt Case Information (OECI) account to search
                            for eviction records with EvictionSponge, otherwise the service is free.
                        </p>
                    </div>
                    <div
                    className="container bg-white rounded pt-4"
                    style={{maxWidth: "560px"}}
                    >
                        <div className="row">
                            <Form className="col">
                                <Form.Group controlId="formBasicEmail">
                                    <Form.Label>Email Address (Required)</Form.Label>
                                    <Form.Control type="email" placeholder="Enter email" />
                                    <Form.Text className="text-muted">
                                        We'll never share your email with anyone else!
                                    </Form.Text>
                                </Form.Group>
                                <Form.Group>
                                    <Form.Label>Name</Form.Label>
                                    <Form.Control placeholder="Enter name" />
                                </Form.Group>
                                <Form.Group>
                                    <Form.Label>Organization</Form.Label>
                                    <Form.Control placeholder="Enter organization name" />
                                </Form.Group>
                                <Form.Group controlId="formBasicCheckbox">
                                    <Form.Check type="checkbox"
                                    label="I'm interested in a demonstration of the software!" />
                                </Form.Group>
                                <Button variant="primary" type="submit">
                                    Submit
                                </Button>
                            </Form>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}