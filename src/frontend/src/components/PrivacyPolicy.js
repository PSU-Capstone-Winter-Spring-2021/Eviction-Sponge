import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import Container from '@material-ui/core/Container';
import Avatar from '@material-ui/core/Avatar';


class PrivacyPolicy extends React.Component {
    render() {
        return (
          <Container >
            <>
            <main className="flex-l mw8 center ph4 mt5">
              <article className="order-1 lh-copy">
                <section className="mb5">
                  <h1 className="f2 fw9 mb3 mt4" id="privacypolicy">
                    Privacy Policy
                  </h1>
                  <p className="mb3">
                    Our privacy policy is simple and meant to be read by all of our
                    users. Please email michael@qiu-qiulaw.com if anything is
                    unclear.
                  </p>
                  <h2 className="f4 fw7 mb2">What we collect and why</h2>
                  <p className="mb3">
                    Our guiding principle is to collect only what we need, and we
                    will not sell your data. Here’s what that means in practice:
                  </p>
                  <h3 className="fw7 mb2">Cookies</h3>
                  <p className="mb3">
                    We use persistent first-party cookies to support necessary
                    functions of the application. A cookie is a piece of text stored
                    by your browser to help it remember your login information, site
                    preferences, and more. You can adjust cookie retention settings
                    in your own browser. To learn more about cookies, including how
                    to see which cookies have been set and how to manage and delete
                    them, please visit:{" "}
                    <a
                      href="https://www.allaboutcookies.org"
                      className="bb hover-blue"
                    >
                      allaboutcookies.org
                    </a>
                    .
                  </p>
                  <h3 className="fw7 mb2">Voluntary correspondence</h3>
                  <p className="mb3">
                    When you write EvictionSponge with a question or to ask for help,
                    we keep that correspondence, including the email address, so
                    that we have a history of past correspondences to reference if
                    you reach out in the future.
                  </p>
                  <h2 className="f4 fw7 mb2">What we don't collect</h2>
                  <p className="mb3">
                    We care about the privacy of your clients’ criminal records.
                    Indeed, this project’s purpose is to make these records more
                    private. Therefore, EvictionSponge does not record or collect
                    search information. If you are using this software for clients,
                    we have no way of identifying who they are.
                  </p>
                  <p className="mb3">
                    We do not save your Oregon eCourt Case Information (OECI) login
                    credentials. That’s why we must separately log in to OECI every
                    time you use EvictionSponge.
                  </p>
                  <h2 className="f4 fw7 mb2">How we secure your data</h2>
                  <p className="mb3">
                    All data is encrypted via SSL/TLS when transmitted from our
                    servers to your browser.
                  </p>
                  <h3>
                    Adapted from the{" "}
                    <a
                      href="https://opensource.org/licenses/MIT"
                      className="bb hover-blue"
                    >
                      MIT License
                    </a>{" "}
                  </h3>
                </section>
    
                <section className="mb5">
                  <h2 className="f2 fw9 mb3" id="license">
                    License
                  </h2>
                  <p className="mb3">Copyright 2020 Michael Zhang, Qiu-Qiu Law</p>
                  <p className="mb3">
                    Permission is hereby granted, free of charge, to any person
                    obtaining a copy of this manual and associated documentation
                    files (the "Manual"), to deal in the Manual without restriction,
                    including without limitation the rights to use, copy, modify,
                    merge, publish, distribute, sublicense, and/or sell copies of
                    the Manual, and to permit persons to whom the Software is
                    furnished to do so, subject to the following conditions:
                  </p>
                  <p className="mb3">
                    The above copyright notice and this permission notice shall be
                    included in all copies or substantial portions of the Manual.
                  </p>
                  <p className="mb4">
                    THE MANUAL IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
                    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
                    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
                    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
                    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
                    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
                    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
                    OTHER DEALINGS IN THE MANUAL.
                  </p>
                  <p className="fw7 mb2">Short list of Credits</p>
                  <ul className="list mb3">
                    <li className="mb2">Thomas Pollard</li>
                    <li className="mb2">Zayne Stites</li>
                    <li className="mb2">Logan Voruz</li>
                    <li className="mb2">Caillie Juergens</li>
                    <li className="mb2">Samuel Youngs</li>
                    <li className="mb2">Ping Chun Chung</li>
                    <li className="mb2">Danford Compton</li>
                    <li className="mb2">Zhengmao Zhang</li>
                    <li className="mb2">Michael Zhang</li>
                  </ul>
                </section>
              </article>
            </main>
          </>
          </Container>
        );
    }
}
export default PrivacyPolicy;