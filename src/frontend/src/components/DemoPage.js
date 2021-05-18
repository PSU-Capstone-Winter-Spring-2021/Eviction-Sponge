import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import Search from './Search';
import Container from '@material-ui/core/Container';

class DemoPage extends React.Component {
    render() {
        return (
        <Container>
          <article className="lh-copy">
              <div className="bg-white shadow bl bw3 b--blue mv4 pv4 ph4 ph5-l br3">
                  <h1 className="f3 fw9 ma0 mb2">App Demo</h1>
                  <p className="mw7 mb3">
                      This demo provides example Eviction that demonstrate the complex
                      rules of expungement and the analysis features of EvictionSponge. The
                      demo version does not search the OECI database, and thus doesn't
                      require an OECI account to use.
                  </p>
                  <p className="mw7 mb3">
                      You can also "Enable Editing" below the search panel to build and
                      evaluate different examples. If you are looking to evaluate your own
                      Eviction for expungement eligibility, we urge you to contact{" "}
                  </p>
                  <p className="mb3 mw7 ">
                      Try searching any of the following examples by entering them in the
                      search panel below.
                  </p>
              </div>
              <div>
              <p className="flex lh-title mb3">
                <div className="mr4">
                  <div className="fw6">First Name</div>
                  <div>Single</div>
                </div>
                <div>
                  <div className="fw6">Last Name</div>
                  <div>Conviction</div>
                </div>
              </p>
              <p className="pb2">
                  As a simple example, if a person's record has only a single
                  convicted charge, it is eligible after three years.
              </p>
            </div>
            <Search demo='true'></Search>
          </article>
        </Container>
        );
    }
}
export default DemoPage;