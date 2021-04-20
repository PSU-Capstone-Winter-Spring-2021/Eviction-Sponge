import React from "react";

export default class InvalidInputs extends React.Component {
    render() {
        return (
            <div role="alert" className="w-100">
                {this.props.contents.map((content, i) => {
                    return (
                        this.props.conditions[i] && (
                            <p key={i} className="alert alert-danger">
                                {content}{""}
                            </p>
                        )
                    );
                })}
            </div>
        );
    }
}