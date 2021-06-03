from pathlib import PurePath
from bs4 import BeautifulSoup
from flask import send_file
from flask.views import MethodView
from crawler.crawler import Crawler


class CaseDetail(MethodView):
    def get(self, case_id):
        # We already have the page cached in Crawler, so just grab the html from there
        url = f"https://publicaccess.courts.oregon.gov/PublicAccessLogin/CaseDetail.aspx?CaseID={case_id}"
        page_html = Crawler.fetch_case_detail_link(url)

        if not page_html:
            return f"Unable to retrieve case detail page for case with ID {case_id}."

        soup = BeautifulSoup(page_html.text, "html.parser")

        # Strip all the links
        for link in soup.findAll("a"):
            link["href"] = "#"

        return soup.prettify()


class CaseDetailCSS(MethodView):
    def get(self):
        path = PurePath(__file__).parent / "resources" / "oeci.css"
        return send_file(str(path), mimetype="text/css")


def register(app):
    app.add_url_rule("/case-detail/<int:case_id>", view_func=CaseDetail.as_view("case-detail"))
    app.add_url_rule("/case-detail/CSS/PublicAccess.css", view_func=CaseDetailCSS.as_view("case-detail-css"))
