import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import Search from './Search';
import Container from '@material-ui/core/Container';

class DemoPage extends React.Component {
    render() {
        return (
          <Container>
          <article className="lh-copy text-left">
              <div className="bg-white bl bw3 b--blue mv4 pv4 ph4 ph5-l br3">
                  <h1 className="f3 fw9 ma0 mb2 text-center">App Demo</h1>
                  <p className="mw7 mb3">
                      This demo provides example Eviction that demonstrate the complex
                      rules of expungement and the analysis features of EvictionSponge. The
                      demo version does not search the OECI database, and thus doesn't
                      require an OECI account to use.
                  </p>
                  <p className="mw7 mb3">
                      You can also "Enable Editing" below the search panel to build and
                      evaluate different examples. If you are looking to evaluate your own
                      Eviction for expungement eligibility, we urge you to contact Michael at <a href='mailto:michael@qiuqiulaw.com'>Michael@quiquilaw.com</a>
                  </p>
                  <p className="mb3 mw7 ">
                      Try searching any of the following examples by entering them in the
                      search panel below.
                  </p>
              </div>
              <div className="flex lh-title mb3 mr4">
                  <p className="fw6">First Name</p>
                  <p>Middle Name (optional)</p>
                  <p className="fw6">Last Name</p>
              </div>
              <div>
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
