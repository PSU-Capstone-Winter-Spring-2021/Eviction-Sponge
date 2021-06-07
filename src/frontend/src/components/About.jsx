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
                        <p>The EvictionSponge development team quickly grew passionate about the project when they learned about the positive
                            impact this software would have on the local community.</p>
                        <p>The team wants to thank Michael Zhang for sponsoring this project and giving them the necessary
                            tools to be successful.</p>
                        <h2>Meet the Team</h2>
                        <div class="row text-left">
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://scontent.fhio2-2.fna.fbcdn.net/v/t1.18169-9/10639514_850907448266229_4213876653792762123_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=FXHyxkl_uxgAX-X3mMt&_nc_ht=scontent.fhio2-2.fna&oh=1bfa89cde8853d15613044ff0292e57b&oe=60E07ED4"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Thomas Pollard</p>
                            <p>Capstone project team lead. Computer science undergraduate at Portland State University, graduated June 2021</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://i.imgur.com/IDFW5cc.jpg"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Zayne Stites</p>
                            <p>Backend developer.  Graduated June 2021.</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://i.imgur.com/n7Ezuyh.jpg"
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
                            <p>Computer science undergraduate at Portland State University, graduated June 2021</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://media-exp1.licdn.com/dms/image/C5603AQGERE1qc0M9wA/profile-displayphoto-shrink_800_800/0/1619299758622?e=1628726400&v=beta&t=Al9PvbMrHfv-EXt2irAUo89yrru8hGSJw9R0iTyoytM"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Samuel Youngs</p>
                            <p>Computer science undergrad and front end developer.</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.kindpng.com/picc/m/144-1447559_profile-icon-missing-profile-picture-icon-hd-png.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Ping Chun Chung</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.kindpng.com/picc/m/144-1447559_profile-icon-missing-profile-picture-icon-hd-png.png"
                                    className="img-responsive" width="250" height="250"/></p>
                            <p>Danford Compton</p>
                            <p>Quis vero earum ullam explicabo. Quae ratione rem illo!</p>
                          </div>
                          </div>
                          <div class="col-sm-6">
                            <div className="col-md-12 well">
                            <p><img src="https://www.kindpng.com/picc/m/144-1447559_profile-icon-missing-profile-picture-icon-hd-png.png"
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