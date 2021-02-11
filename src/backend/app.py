from os import path
from flask import Flask

from endpoints import hello, static

FRONTEND_BUILD_DIR = path.abspath(path.join(path.dirname(__file__), "..", "frontend"))

def create_app():
    app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR)

<<<<<<< HEAD
    if __name__ == '__main__':
      app.run(host = 'localhost', port = '5000')
      
    # Main page
    @app.route('/')
    def index():
      return 'Homepage'


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
=======
    hello.register(app)
    static.register(app)
>>>>>>> backendstart

    return app

if __name__ == '__main__':
    application = create_app()
    application.run(host="localhost", port=5000, debug=True)
