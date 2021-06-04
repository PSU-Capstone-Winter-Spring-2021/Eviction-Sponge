import React from "react";

class About extends React.Component {

    componentDidMount(){
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
                        <p>The EvictionSponge development team quickly grew passionate about the project  when they learned about the positive
                            impact this software would have on the local community.</p>
                        <p>The team wants to thank Michael Zhang for sponsoring this project and giving them the necessary
                            tools to be successful.</p>
                        <h2>Meet the Team</h2>
                        <div class="row text-left">
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Thomas Pollard</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Zayne Stites</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                 className="img-responsive" width="250" height="250"/></p>
                            <p>Logan Voruz</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://i.imgur.com/FC9HJSm.jpg"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Caillie Juergens</p>
                            <p>Computer Science Undergraduate at Portland State University, Class of '21</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Samuel Youngs</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Ping Chun Chung</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Danford Compton</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.freepnglogos.com/uploads/spongebob-png/photo-editing-effects-master-effetcs-spongebob-25.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Zhengmao Zhang</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
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