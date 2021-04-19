import src

class EndpointShared:
    def __init__ (self):
        self.app = src.creat_app("development")
        self.client = self.app.test_client()
