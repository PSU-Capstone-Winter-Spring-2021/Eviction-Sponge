import React from "react";

class Landing extends React.Component {
    componentDidMount() {
        document.title="EvictionSponge";
    }
    render() {
        return (
            <>
                <main>
                    <h1>EvictionSponge</h1>
                    <div>This is the eviction sponge landing page</div>
                </main>
            </>
        );
    }
}

export default Landing;