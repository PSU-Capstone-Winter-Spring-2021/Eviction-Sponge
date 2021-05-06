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
        <>
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
                    <section>
                    <div
                    className="container bg-white rounded pt-4"
                    style={{maxWidth: "560px"}}>
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
                </section>
                <section>
                    <div
                    className="container bg-white rounded pt-4"
                    style={{maxWidth: "560px"}}>

                    <div className="" id="mc_embed_signup">
                    {" "}
                    {/* This section is based on Mailchimp's generated Embed html*/}
                        <form
                            action="https://gmail.us1.list-manage.com/subscribe/post?u=c986b937167b4fa39b4cee9ad&amp;id=b51d1594ae"
                            method="post"
                            id="mc-embedded-subscribe-form"
                            name="mc-embedded-subscribe-form"
                            className=""
                            target="_blank"
                            noValidate
                        >
                    <div
                        className="bg-white shadow br3 pb5 mb3"
                        id="mc_embed_signup_scroll"
                    >
                    <span className="db center bb bw3 b--blue mb4"/>
                    <div className="ph4 ph5-ns ph6-l">
                      <div className="mb3 mc-field-group">
                        <label className="db fw6 mb1" htmlFor="mce-EMAIL">
                          Email Address (Required)
                        </label>
                        <input
                          type="email"
                          name="EMAIL"
                          className="w-100 b--black-20 br2 pa3 required email"
                          id="mce-EMAIL"
                          placeholder="Enter email"
                          onChange={(e: React.BaseSyntheticEvent) => {
                            this.setState({
                              email: e.target.value,
                              invalidEmail: false,
                            });
                          }}
                        />
                      </div>
                      <div className="mb3 mc-field-group">
                        <label className="db fw6 mb1" htmlFor="mce-NAME">
                          Name{" "}
                        </label>
                        <input
                          type="text"
                          name="NAME"
                          className="w-100 b--black-20 br2 pa3"
                          id="mce-NAME"
                          placeholder="Enter name"
                        />
                      </div>
                      <div className="mb2 mc-field-group">
                        <label className="db fw6 mb1" htmlFor="mce-ORG">
                          Organization{" "}
                        </label>
                        <input
                          type="text"
                          name="ORG"
                          className="w-100 b--black-20 br2 pa3"
                          id="mce-ORG"
                          placeholder="Enter organization name"
                        />
                      </div>
                      <div className="checkbox mb4 mc-field-group input-group">
                        <input
                          type="checkbox"
                          value="1"
                          name="group[19029][1]"
                          id="mce-group[19029]-19029-0"
                        />
                        <label
                          className="fw6"
                          htmlFor="mce-group[19029]-19029-0"
                        >
                          I'm interested in a demonstration of the software!
                        </label>
                      </div>
                      <div id="mce-responses" className="clear">
                        <div
                            className="response"
                            id="mce-error-response"
                            visually-hidden
                        />
                        <div
                            className="response"
                            id="mce-success-response"
                            visually-hidden
                        />
                      </div>{" "}
                      {/*This div captures bot signups, according to Mailchimp.*/}
                      <div className="clear">
                        <input
                          type="submit"
                          value="Submit"
                          name="submit"
                          id="mc-embedded-submit"
                          className="w-100 pointer bg-blue white bg-animate hover-bg-dark-blue bn fw6 br2 pv3 ph4"
                          onClick={this.handleSubmit}
                        />
                      </div>
                    </div>
                  </div>
                </form>
              </div>
                    </div>
            </section>

                </div>

            </div>

            </>


        );
    }
}