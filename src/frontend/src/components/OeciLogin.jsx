import React from "react";


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
    handleSubmit(event) {
        event.preventDefault();
        const data = new FormData(event.target);

        fetch('/api/form-submit-url', {
            method: 'POST',
            body: data,
        });
    }

    // HTML(?) for the component
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    User ID:
                </label>
                <input
                    id="userId"
                    name="oecilogin"
                    type="text"
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
                    value={this.state.password}
                    onChange={this.onChange}
                />
                <input type="submit" value="Log In" />
            </form>
        )
    }
}

export default OeciLogin;