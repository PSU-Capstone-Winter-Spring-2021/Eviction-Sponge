import React from "react";

class About extends React.Component {

    componentDidMount() {
        document.title = "About - EvictionSponge";
    }

    render() {
        return (
            <main className="container bg-light w-100 m-0 mw-100 px-0 mh57">
                <div className="row mx-0 justify-content-center">
                    <div className="col-md-8 text-left col-md-offset-2">
                        <h1>EvictionSponge provides a resource for
                        eviction record expungement in Oregon
                        </h1>
                        <p>The eviction sponge project is a web-hosted
                        service that allows users to check their
                        eligibility for eviction record expungement
                        and, if they are eligible, provides the
                        necessary legal documentation auto-filled with their information.
                        </p>
                        <h2>Our Mission</h2>
                        <p>This website began as a senior project for eight undergraduate computer science
                            students at Portland State University in the beginning of 2021. </p>
                        <p>The EvictionSponge development team quickly grew passionate about the project when they learned about the positive
                            impact this software would have on the local community.</p>
                        <p>The team wants to thank Michael Zhang for sponsoring this project and giving them the necessary
                            tools to be successful.</p>
                        <h2>Meet the Team</h2>
                        <div class="row text-left">
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/ayXf4pz.jpg"
                                        className="img-responsive" alt="Thomas Pollard" width="250" height="250" /></p>
                                    <p>Thomas Pollard</p>
                                    <p>Capstone project team lead. Computer science undergraduate at Portland State University, graduated June 2021</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/IDFW5cc.jpg"
                                        className="img-responsive" alt="Zayne Stites" width="250" height="250" /></p>
                                    <p>Zayne Stites</p>
                                    <p>Backend developer.  Graduated June 2021.</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/Ytrq24C.jpg"
                                        className="img-responsive" alt="Logan Voruz" width="250" height="250" /></p>
                                    <p>Logan Voruz</p>
                                    <p>Frontend Developer, Computer Science undergraduate at Portland State University, class of 2021</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/FC9HJSm.jpg"
                                        className="img-responsive" alt="Caillie Juergens" width="250" height="250" /></p>
                                    <p>Caillie Juergens</p>
                                    <p>Computer science undergraduate at Portland State University, graduated June 2021</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/9PJCYu9.jpg"
                                        className="img-responsive" alt="Samuel Youngs" maxwidth="250" height="250" /></p>
                                    <p>Samuel Youngs</p>
                                    <p>Computer science undergrad and front end developer.</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/NG4c1xv.jpg"
                                        className="img-responsive" alt="Ping Chun Chung" width="250" height="250" /></p>
                                    <p>Ping Chun Chung</p>
                                    <p>Computer science undergrad at Portland State University</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://i.imgur.com/WOSKxmJ.jpg"
                                        className="img-responsive" alt="Danford Compton" width="250" height="250" /></p>
                                    <p>Danford Compton</p>
                                    <p>Backend developer, computer science undergrad, Portland State University class of 2021</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div className="col-md-12 well">
                                    <p><img src="https://scontent.fhio2-1.fna.fbcdn.net/v/t1.18169-9/22046575_765710706964789_2717801391033859401_n.jpg?_nc_cat=103&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=gv3ehxCyy00AX--IgDg&_nc_ht=scontent.fhio2-1.fna&oh=0d9a839229549fbfb3c3c7dcd76cb8eb&oe=60E28127"
                                        className="img-responsive" alt="Zhengmao Zhang" width="250" height="250" /></p>
                                    <p>Zhengmao Zhang</p>
                                    <p>Computer science undergraduate at Portland State University and Changchun University of Technology, graduated June 2021</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        );
    }
}

export default About;
