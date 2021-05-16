import React from "react";
import "bootstrap/dist/css/bootstrap.css";

class Accessibility extends React.Component {
    render() {
        return (
            <main>
                <h2>Accessibility Statement for <span class="basic-information website-name">EvictionSponge</span></h2>
                <p>This is an accessibility statement from <span class="basic-information organization-name">Eviction Sponge</span>.</p>
                <h3>Conformance status</h3>
                <p>The
                    <a href="https://www.w3.org/WAI/standards-guidelines/wcag/">Web Content Accessibility Guidelines
                        (WCAG)
                    </a>
                    defines requirements for designers and developers to improve accessibility for people with disabilities.
                    It defines three levels of conformance: Level A, Level AA, and Level AAA.
                    <span class="basic-information website-name">EvictionSponge</span>
                    is
                    <span class="basic-information conformance-status" data-printfilter="lowercase">partially conformant</span>
                    with
                    <span class="basic-information conformance-standard">
                                    <span data-negate="">WCAG 2.1 level AA</span>.
                                </span>
                    <span>
                                    <span class="basic-information conformance-status">Partially conformant</span>
                                    means that
	                            <span class="basic-information conformance-meaning">some parts of the content do not fully conform to the accessibility standard</span>.
                                </span>
                </p>
                <h3>Feedback</h3>
                <p>
                    We welcome your feedback on the accessibility of
                    <span class="basic-information website-name">EvictionSponge</span>.
                    Please let us know if you encounter accessibility barriers on
                    <span class="basic-information website-name">EvictionSponge</span>:
                </p>
                <ul class="basic-information feedback h-card">
                    <li>
                        E-mail:
                        <a class="email u-email" href="mailto:contact@evictionsponge.com">contact@evictionsponge.com</a>
                    </li>
                </ul>
                <h3>Technical specifications</h3>
                <p>
                    Accessibility of
                    <span class="basic-information website-name">EvictionSponge</span>
                    relies on the following technologies to work with the particular combination of web browser and any assistive
                    technologies or plugins installed on your computer:
                </p>
                <ul class="technical-information technologies-used">
                    <li>HTML</li>
                    <li>WAI-ARIA</li>
                    <li>CSS</li>
                    <li>JavaScript</li>
                </ul>
                <p>These technologies are relied upon for conformance with the accessibility standards used.</p>
                <h3>Assessment approach</h3>
                <p>
                    <span class="basic-information organization-name">Eviction Sponge</span>
                    assessed the accessibility of
                    <span class="basic-information website-name">EvictionSponge</span>
                    by the following approaches:
                </p>
                <ul class="technical-information assessment-approaches">
                    <li>Self-evaluation</li>
                </ul>
                {/* <hr noshade="noshade"> */}
                    <h3>Date</h3>
                {/* </hr> */}
            </main>
        );
    }
}

export default Accessibility;
