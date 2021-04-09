from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify

from src.backend.crawler.crawler import Crawler, UnableToReachOECI, InvalidLoginCreds

import os

from src.backend.crypto import DataCipher

# log an error message and stop process
def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


class OeciLogin(MethodView):
    def post(self):
        data = request.form
        print(request.cookies)

        # Check for data validity:
        if data is None:
            error(400, "Missing one or more required fields")
        if data.get('oecilogin') is None:
            error(400, "Missing OECI login username")
        if data.get('oecipassword') is None:
            error(400, "Missing OECI login password")

        response = make_response()
        credentials = {'username': data['oecilogin'], 'password': data['oecipassword']}

        cipher = DataCipher(key=current_app.config.get("SECRET_KEY"))
        encrypted_credentials = cipher.encrypt(credentials)

        # Try to log into OECI database
        try:
            Crawler.attempt_login(credentials['username'], credentials['password'])
            response.set_cookie(
                "oeci_token",
                secure=os.getenv("TIER") == "production",
                samesite="strict",
                value=encrypted_credentials
            )
        except UnableToReachOECI:
            error(404, "Unable to reach OECI database")
        except InvalidLoginCreds:
            error(401, "Invalid login credentials")

        return response, 201


def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
