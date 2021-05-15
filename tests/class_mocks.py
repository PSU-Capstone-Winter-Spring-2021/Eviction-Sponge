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
    date: date
    violation_type: str
    current_status: str
    judgements: List[str]
    case_detail_link: str
    balance_due_in_cents: int

    def __init__(self, case_num, style, location, date, case_type, status, judgements, case_detail_link):
        self.case_number = case_num
        self.style = style
        self.location = location
        self.date = date
        self.violation_type = case_type
        self.current_status = status
        self.judgements = judgements
        self.case_detail_link = case_detail_link
        self.balance_due_in_cents = 0
