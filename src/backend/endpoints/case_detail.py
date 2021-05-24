from bs4 import BeautifulSoup
from flask.views import MethodView

from crawler.crawler import Crawler


class CaseDetail(MethodView):
    def get(self, case_id):
        # We already have the page cached in Crawler, so just grab the html from there
        url = 'https://publicaccess.courts.oregon.gov/PublicAccessLogin/CaseDetail.aspx?CaseID=' + case_id
        page_html = Crawler.fetch_case_detail_link(url)

        if not page_html:
            return "Unable to retrieve case detail page for case with ID " + case_id + "."

        soup = BeautifulSoup(page_html.text, "html.parser")

        # Strip all the links
        for link in soup.findAll('a'):
            del link['href']

        return soup


def register(app):
    app.add_url_rule("/case-detail", view_func=CaseDetail.as_view("case-detail"))