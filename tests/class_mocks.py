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
