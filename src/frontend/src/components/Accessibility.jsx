import React from "react";

class Accessibility extends React.Component {

    componentDidMount(){
        document.title = "Accessibility Statement - EvictionSponge";
    }

    render() {
        return (
            <main className = "container bg-light text-left font-weight-light" style = {{maxWidth: "720px"}}>
                <section>
                    <h1 className = "font-weight-bold mb-4" style = {{maxWidth: "420px"}}>Accessibility Statement for <span className="basic-information website-name">EvictionSponge</span></h1>
                    <p className = "mb-4">This is an accessibility statement from <span className="basic-information organization-name">Eviction Sponge</span>.</p>
                </section>
                <section>
                <h2 className = "font-weight-bold mb-4">Conformance status</h2>
                <p className = "mb-4">The
                    <a href="https://www.w3.org/WAI/standards-guidelines/wcag/"> Web Content Accessibility Guidelines
                        (WCAG)
                    </a>
                     defines requirements for designers and developers to improve accessibility for people with disabilities.
                    It defines three levels of conformance: Level A, Level AA, and Level AAA.
                    <span className="basic-information website-name">EvictionSponge </span>
                    is
                    <span className="basic-information conformance-status" data-printfilter="lowercase"> partially conformant </span>
                    with
                    <span className="basic-information conformance-standard">
                                    <span data-negate=""> WCAG 2.1 level AA</span>.
                                </span>
                    <span>
                                    <span className="basic-information conformance-status"> Partially conformant </span>
                                    means that
	                            <span className="basic-information conformance-meaning"> some parts of the content do not fully conform to the accessibility standard</span>.
                                </span>
                </p>
                </section>
                <section>
                    <h2 className = "font-weight-bold mb-4">Feedback</h2>
                    <p className = "mb-4">
                        We welcome your feedback on the accessibility of
                        <span className="basic-information website-name">EvictionSponge</span>.
                        Please let us know if you encounter accessibility barriers on
                        <span className="basic-information website-name">EvictionSponge</span>:
                    </p>
                    <ul className="basic-information feedback h-card mb-4">
                        <li>
                            E-mail:
                            <a className="email u-email" href="mailto:contact@evictionsponge.com">contact@evictionsponge.com</a>
                        </li>
                    </ul>
                </section>
                <section>
                    <h2 className = "font-weight-bold mb-4">Technical specifications</h2>
                    <p className = "mb-4">
                        Accessibility of
                        <span className="basic-information website-name">EvictionSponge</span>
                        relies on the following technologies to work with the particular combination of web browser and any assistive
                        technologies or plugins installed on your computer:
                    </p>
                    <ul className="technical-information technologies-used mb-4">
                        <li>HTML</li>
                        <li>WAI-ARIA</li>
                        <li>CSS</li>
                        <li>JavaScript</li>
                    </ul>
                    <p className = "mb-4">These technologies are relied upon for conformance with the accessibility standards used.</p>
                </section>
                <section>
                    <h2 className = "font-weight-bold mb-4">Assessment approach</h2>
                    <p className = "mb-4">
                        <span className="basic-information organization-name">Eviction Sponge</span>
                        assessed the accessibility of
                        <span className="basic-information website-name"> EvictionSponge </span>
                        by the following approaches:
                    </p>
                    <ul className="technical-information assessment-approaches mb-4">
                        <li>Self-evaluation</li>
                    </ul>
                </section>
            </main>
        );
    }
}

export default Accessibility;
