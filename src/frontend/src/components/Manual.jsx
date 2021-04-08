import React from "react";
import "bootstrap/dist/css/bootstrap.css";

class Manual extends React.Component {

    constructor(props) {
        // TODO: Figure out what arguments go into the super call
        super(props);
    };

    componentDidMount(){
        // document.title is the string in the tab, update it to reflect current component
        document.title = "Manual"
    };

    // HTML for the component
    render() {
        return (
            <div className="container bg-light w-100 m-0 mw-100 px-0">
                <div className="row mx-0">
                    <div className="col border d-xs-block d-sm-none">
                        <nav>
                            <ul className="list-unstyled">
                            <li>
                                <a href="#introduction">
                                Introduction
                                </a>
                            </li>
                            <li>
                                <a href="#information">
                                General Information
                                </a>
                            </li>
                            <li>
                                <a href="#howto">
                                How to Use EvictionSponge
                                </a>
                            </li>
                            <li>
                                <a href="#assumptions">
                                Assumptions
                                </a>
                            </li>
                            <li>
                                <a href="#search">
                                Search
                                </a>
                            </li>
                            <li>
                                <a href="#file">
                                File for Eviction Expungement
                                </a>
                            </li>
                            </ul>
                        </nav>
                    </div>
                </div>
                <div className="row mx-0 justify-content-center">
                    <div className="col-sm-6 text-left">
                        <div>
                            <h2 id="introduction">
                                Introduction
                            </h2>
                            <p className="font-weight-light">
                            EvictionSponge is a web application used to facilitate the expungement process for evictions that occured in Oregon. It is built by a team of students at PSU for their capstone project and is based on the RecordSponge project by Code for PDX. The codebase is published under an open source MIT license.
                            <br />This Manual explains how EvictionSponge is used and the process of expunging eviction records. 
                            </p>
                        </div>
                        <div className="">
                            <h2>General Info</h2>
                            <p>
                                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Enim atque, autem dolor ab voluptatem voluptas officiis esse fugiat quos quisquam eligendi ea quasi aut labore cum mollitia impedit dolorum a.
                                Debitis, nisi nobis a deleniti quam accusantium veniam dignissimos consectetur sit delectus, quidem voluptatum unde laborum aliquid illo quo molestiae perspiciatis! Quis vero earum ullam explicabo. Quae ratione rem illo!
                                Aut ratione veritatis necessitatibus ipsam! Sunt assumenda fuga omnis odit voluptatem temporibus nulla quaerat minima vitae corporis debitis cum quas illo nisi consequuntur, unde esse officia, alias nemo recusandae laboriosam.
                                Officia error reprehenderit pariatur ab! Minus dolor distinctio ipsa reiciendis hic in aliquid sunt tenetur praesentium, omnis eum vel asperiores illo deserunt quos perferendis laboriosam. Est corporis similique iusto rem.
                                Magnam, nulla tempore, est atque vitae facere tenetur consequatur iste itaque, velit obcaecati omnis et dolorum ratione quis minima? Dicta deserunt magnam eius quasi! Vel enim quia ut animi ipsum!
                                Eum ex consectetur nihil dolor dolore voluptas fugiat, rerum hic sed iure obcaecati error quis tenetur eveniet sunt animi reiciendis mollitia quod ipsa qui tempora quae cum illum! Eligendi, asperiores.
                                Dolores dolore, inventore illum consequuntur eius soluta distinctio! Quidem, repudiandae ad. Earum optio exercitationem expedita quis, veniam doloremque, harum ea eaque laborum hic consequatur placeat incidunt deleniti maxime nulla iure?
                                Dolorum magni dicta, illo delectus iure eos ut ipsa placeat, consectetur atque doloribus ducimus sed dolorem neque voluptatem! Molestiae ullam nihil eligendi neque accusantium pariatur, cumque asperiores ducimus error nam!
                            </p>
                        </div>
                        <div>
                            <h2 id="howto">How to Use EvictionSponge</h2>
                            <p>how to use text</p>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi, cupiditate.
                            Molestias eos animi voluptatum quo consectetur eveniet quibusdam tempore neque!
                            Culpa voluptate quas molestias explicabo provident vero eos optio. Modi?
                            Non blanditiis aperiam pariatur autem ex quisquam magni assumenda commodi.
                            Optio est, quos sapiente ab doloremque odit. Natus, consectetur ratione!
                            Praesentium voluptates, non tenetur reiciendis alias quas asperiores cumque atque.
                            Quisquam nesciunt sit harum beatae pariatur! Non id nam aperiam?
                            Ab, libero fuga? Magnam molestiae, nisi iure quos quaerat sed?
                            Libero numquam cum architecto illum iusto velit aut maiores laborum?
                            Quae, atque? Blanditiis deserunt ipsum in molestiae saepe magni enim?
                            <h2>Assumptions</h2>
                            <ul>
                                <li>
                                    <h3>Assumption 1</h3>
                                </li>
                                <li>
                                    <h3>Assumption 2</h3>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div className="col-3 border d-none d-sm-block sticky-top h-25">
                        <nav>
                            <ul className="list-unstyled text-left">
                            <li>
                                <a href="#introduction">
                                Introduction
                                </a>
                            </li>
                            <li>
                                <a href="#information">
                                General Information
                                </a>
                            </li>
                            <li>
                                <a href="#howto">
                                How to Use EvictionSponge
                                </a>
                            </li>
                            <li>
                                <a href="#assumptions">
                                Assumptions
                                </a>
                            </li>
                            <li>
                                <a href="#search">
                                Search
                                </a>
                            </li>
                            <li>
                                <a href="#file">
                                File for Eviction Expungement
                                </a>
                            </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        )
    }
}

export default Manual;