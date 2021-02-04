from os import path
from flask import Flask

from endpoints import hello, static

FRONTEND_BUILD_DIR = path.abspath(path.join(path.dirname(__file__), "..", "frontend"))

def create_app():
    app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR)

    hello.register(app)
    static.register(app)

    return app

if __name__ == '__main__':
    application = create_app()
    application.run(host="localhost", port=5000, debug=True)
