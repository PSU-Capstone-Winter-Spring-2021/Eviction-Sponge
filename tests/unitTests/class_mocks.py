# Various mock classes for unit testing the crawler

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


class MockCaseSummary:
    case_num = ""  # Declaring these outside of init as well for ease of testing
    style = ""
    date_location = []
    type_status = []
    case_detail_link = ""

    def __init__(self, case_num, style, date_location, type_status, case_detail_link):
        self.case_num = case_num
        self.style = style
        self.date_location = date_location
        self.type_status = type_status
        self.case_detail_link = case_detail_link


class MockCaseDetail:
    case_num = "" # Declaring these outside of init as well for ease of testing
    style = ""
    location = ""
    date = None
    judgements = []
    eligibility = None

    def __init__(self, case_num, style, location, date, judgements, eligibility):
        self.case_num = case_num
        self.style = style
        self.location = location
        self.date = date
        self.judgements = judgements
        self.eligibility = eligibility
