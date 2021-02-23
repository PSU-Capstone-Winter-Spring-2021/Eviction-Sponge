from flask.views import MethodView
from flask import request, make_response, current_app
import json

from crawler.crawler import Crawler

class OeciLogin(MethodView):
    def post(self):
        data = request.form
        print(request.cookies)

        response = make_response()
        # Check for data validity:
        if data is None:
            current_app.logger.error("400: Missing one or more required fields")
        if data['oecilogin'] is None:
            current_app.logger.error("400: Missing OECI login username")
        if data['oecipassword'] is None:
            current_app.logger.error("400: Missing OECI login password")

        credentials = {'username': data['oecilogin'], 'password': data['oecipassword']}
        # TODO: encrypt credentials
        credentials_string = json.dumps(credentials)
        print(credentials)

        if Crawler.attempt_login(data['oecilogin'], data['oecipassword']) == 0:
            response.set_cookie(
                "oeci_token",
                samesite="strict",
                value=credentials_string
            )
        else:
            current_app.logger.error("400: OECI login attempt failed")

        return response, 201



def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
