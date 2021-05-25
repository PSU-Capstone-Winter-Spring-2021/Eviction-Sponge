# Various mock classes for backend testing
from typing import List
from datetime import date

class MockRequest:
    text = ""

    def set_text(self, value):
        self.text = value


class MockSession:
    postReturn = None

    def post(self, url, paylord):
        return self.postReturn

    def set_post_return(self, value):
        self.postReturn = value


class MockURL:
    def login_url(self):
        return "login url"

    def search_url(self):
        return "search url"


# TODO: expand this once money parser is working
class MockCaseSummary:
    name: str
    case_number: str
    style: str
    location: str
    complaint_date = str
    closed_date: date
    violation_type: str
    current_status: str
    judgements: List[str]
    case_detail_link: str
    balance_due: str

    def __init__(self, case_num, style, location, complaint_date, closed_date, case_type, status, judgements, case_detail_link, balance_due=""):
        self.case_number = case_num
        self.style = style
        self.location = location
        self.complaint_date = complaint_date
        self.closed_date = closed_date
        self.violation_type = case_type
        self.current_status = status
        self.judgements = judgements
        self.case_detail_link = case_detail_link
        self.balance = balance_due
# Used to mock BeautifulSoup. Functions individually mocked over to adjust return value
class MockSoup:
    def find_all(self, arg1, arg2):
        return None

    def find(self, arg1, headers):
        return None


# Used to mock BeautifulSoup's find_all return. Functions are individually mocked over to adjust return value
class MockTag:
    parent = None
    content = None

    def __init__(self, data=None):
        self.parent = MockTag
        self.content = data

    @staticmethod
    def find(arg1, headers):
        return None

    # _parse_closed_date calls renderContents two times and needs two different return types, so we gotta be fancy here
    def renderContents(self):
        if self.content is not None:
            return self.content
        return None

    def setParent(self, parent):
        self.parent = parent
