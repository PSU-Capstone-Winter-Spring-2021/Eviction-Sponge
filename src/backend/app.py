from os import path
from flask import Flask, request, make_response

from endpoints import hello, static, oeci_login

FRONTEND_BUILD_DIR = path.abspath(path.join(path.dirname(__file__), "..", "frontend", "build"))

def create_app():
    app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR)

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
    application = create_app()
    application.run(host="localhost", port=5000, debug=True)
