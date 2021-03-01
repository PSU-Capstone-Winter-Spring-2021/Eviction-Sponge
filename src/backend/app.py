from os import path, getenv
from flask import Flask, request, make_response

from config import app_config
from endpoints import hello, static, oeci_login

FRONTEND_BUILD_DIR = path.abspath(path.join(path.dirname(__file__), "..", "frontend", "build"))

def create_app(env_name):
    app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR)
    app.config.from_object(app_config[env_name])
    # @app.route('/api/form-submit-url', methods=['POST'])
    # def handleLogin():
    #     print("login attempted with user", request.form['oecilogin'], "and password", request.form['oecipassword'])
    #     response = make_response()
    #     response.set_cookie(
    #         "oeci_token",
    #         #secure=os.getenv("TIER") == "production",
    #         #httponly=False,
    #         #samesite="strict",
    #         #value=encrypted_credentials,
    #         value="Test Cookie. <TODO> Set encrypted credentials here"
    #     )
    #     response.set_cookie("test", "success")
    #     return response, 201


    hello.register(app)
    static.register(app)
    oeci_login.register(app)

    return app

if __name__ == '__main__':
    tier = getenv("TIER", default="development")
    application = create_app(tier)
    application.run(host="localhost", port=5000)
