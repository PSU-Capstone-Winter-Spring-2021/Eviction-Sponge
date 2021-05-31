import React from "react";
import {redirectSearch} from "../cookieService";

class OeciLogin extends React.Component {

    state = {
        userId: "",
        password: "",
    };

    constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
        this.state= {value: ''};

        this.onChange = this.onChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    };

    componentDidMount(){
        document.title = "OECI Login - EvictionSponge";
    };

    onChange = (e) => {
        this.setState({ value: e.target.value });
        // So, afaik onChange calls handleChange automatically. Some sites recommend this code tidbit be in onChange,
        // others in handleChange. Not sure why.
    };

    // gather all the user-entered data and post it for the backend to deal with
    async handleSubmit(event) {
        event.preventDefault();
        const data = new FormData(event.target);

        //fetch('/api/form-submit-url', {
        const response = await fetch('/login', {
            method: 'POST',
            body: data,
        });
        if(response.status == 201){
            redirectSearch();
        }
    }

    // HTML(?) for the component
    render() {
        return (
            <main className="row">
            <form className="col-md-6 bg-darker-green min-vh-100" onSubmit={this.handleSubmit}>
                <div className="d-flex flex-row text-color-white mt-5 mb-3">
                    <h4 className="col">OECI Login</h4>
                </div>
                <div className="d-flex flex-row justify-content-center text-color-white mb-5">
                    <p className="col" style={{maxWidth:"500px"}}>Login to Oeci to search and analyse eviction records for expungement</p>
                </div>
                <div className="d-flex flex-row justify-content-center mt-5 mb-4 text-left">
                    <label className="col-lg-3 text-color-white font-weight-bold">
                        User ID:
                    </label>
                    <input
                        className="col-lg-3"
                        id="userId"
                        name="oecilogin"
                        type="text"
                        placeholder="User ID"
                        value={this.state.userId}
                        onChange={this.onChange}
                    />
                </div>
                <div className="d-flex flex-row justify-content-center mb-4 text-left">
                    <label className="col-lg-3 text-color-white font-weight-bold">
                        Password:
                    </label>
                    <input
                        className="col-lg-3"
                        id="password"
                        name="oecipassword"
                        type="password"
                        placeholder = "Password"
                        value={this.state.password}
                        onChange={this.onChange}
                    />
                </div>
                <div className = "d-flex flex-row justify-content-center mb-5">
                    <div className="col-lg-3"></div>
                    <input className="col-lg-3 btn btn-success" type="submit" value="Log In" />
                </div>
                <div className = "d-flex flex-row justify-content-center text-color-white">
                    <p className="col"  style={{maxWidth:"500px"}}>
                        The eCourt site is offline during the 4th weekend of each month between
                        6 PM PST on Friday until noon on Sunday. During this time, record search
                        will not function.
                    </p>
                </div>
            </form>
            <div className="col-md-6 bg-light min-vh-100 align-self-start">
                <div className="d-flex flex-row justify-content-center mt-4">
                    <h1 className="col">New Here?</h1>
                </div>
                <div className="d-flex flex-row justify-content-center mt-4">
                    <p className="col" style={{maxWidth:"500px"}}>
                        EvictionSponge requires an OECI account to function.
                    </p>
                </div>
                <div className="d-flex flex-row justify-content-center mt-4">
                    <p className="col" style={{maxWidth:"500px"}}>
                        If you don't have one already, you can <br/>
                        <a href="https://www.courts.oregon.gov/services/online/Pages/ojcin-signup.aspx">
                            purchase a subscription here.
                        </a>
                    </p>
                </div>
            </div>
            </main>
        )
    }
}

export default OeciLogin;