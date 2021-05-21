# Various mock classes for unit testing

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


# Used to mock BeautifulSoup. Functions individually mocked over to adjust return value
class MockSoup:
    def find_all(self, arg1, arg2):
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
