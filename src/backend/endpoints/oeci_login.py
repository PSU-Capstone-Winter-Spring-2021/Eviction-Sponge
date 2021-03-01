from flask.views import MethodView
from flask import request, make_response, current_app
import os

from crawler.crawler import Crawler
from crypto import DataCipher


class OeciLogin(MethodView):
    def post(self):
        data = request.form

        # Check for data validity:
        if data is None:
            current_app.logger.error("400: Missing one or more required fields")
        if data.get('oecilogin') is None:
            current_app.logger.error("400: Missing OECI login username")
        if data.get('oecipassword') is None:
            current_app.logger.error("400: Missing OECI login password")

        response = make_response()
        credentials = {'username': data['oecilogin'], 'password': data['oecipassword']}
        cipher = DataCipher(key=current_app.config.get("SECRET_KEY"))
        encrypted_credentials = cipher.encrypt(credentials)

        if Crawler.attempt_login(data['oecilogin'], data['oecipassword']) == 0:
            response.set_cookie(
                "oeci_token",
                secure=os.getenv("TIER") == "production",
                samesite="strict",
                value=encrypted_credentials
            )
        else:
            current_app.logger.error("400: OECI login attempt failed")

        return response, 201



def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
