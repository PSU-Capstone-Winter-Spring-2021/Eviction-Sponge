import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

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

    return app
