import React from "react";


class OeciLogin extends React.Component {

    state = {
        userId: "",
        password: "",
    };

    constructor() {
        // TODO: Figure out what arguments go into the super call
        super({}, {});
        this.handleSubmit = this.handleSubmit.bind(this);
    };

    componentDidMount(){
        // document.title is the string in the tab, update it to reflect current component
        document.title = "OECI Login"
    };

    onChange = (e) => {
        // @ts-ignore // TODO: can't figure out why this.setState({}) makes it unhappy
        this.setState({ text: e.currentTarget.value });
        // So, afaik onChange calls handleChange automatically. Some sites recommend this code tidbit be in onChange,
        // others in handleChange. Not sure why.
    };

    // gather all the user-entered data and post it for the backend to deal with
    handleSubmit(event) {
        event.preventDefault();
        // @ts-ignore // TODO: can't figure out why this.setState({}) makes it unhappy
        const data = new FormData(event.target);

        fetch('/api/form-submit-url', {
            method: 'POST',
            body: data,
        });
    }

    // HTML(?) for the component
    render() {
        return (
            <form>
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
                    name="oecilogin"
                    type="text"
                    value={this.state.password}
                    onChange={this.onChange}
                />
                <button> Submit </button>
            </form>
        )
    }
}

export default OeciLogin;