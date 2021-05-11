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
        // document.title is the string in the tab, update it to reflect current component
        document.title = "OECI Login"
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
            <main className="oeci-login-container p-3">
            <form onSubmit={this.handleSubmit}>
                <label>
                    User ID:
                </label>
                <input
                    id="userId"
                    name="oecilogin"
                    type="text"
                    placeholder="User ID"
                    value={this.state.userId}
                    onChange={this.onChange}
                />
                <label>
                    Password:
                </label>
                <input
                    id="password"
                    name="oecipassword"
                    type="password"
                    placeholder = "Password"
                    value={this.state.password}
                    onChange={this.onChange}
                />
                <input type="submit" value="Log In" />
            </form>
            </main>
        )
    }
}

export default OeciLogin;