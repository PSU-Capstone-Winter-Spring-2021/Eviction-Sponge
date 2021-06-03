from src.backend import app

class EndpointShared:
    def __init__(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client()