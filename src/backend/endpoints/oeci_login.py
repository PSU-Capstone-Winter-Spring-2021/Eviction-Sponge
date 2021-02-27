from flask.views import MethodView
from flask import request, make_response, current_app
from src.backend.crawler import Crawler


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
        #print(credentials)
        result = Crawler.attempt_login(credentials['username'], credentials['password'])
        if result == 1: # if login failed
            current_app.logger.error("Error 401: unable to login to OCEI database")
            # TODO: separate login fail due to invalid credentials and login failied due to unable to reach database

        response.set_cookie("test", "success")
        return response, 201


def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
