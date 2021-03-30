from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import requests
from requests import Session
from src.backend.crypto import DataCipher
from src.backend.crawler import Crawler
import os


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


class Search(MethodView):
    def post(self):
        data = request.get_json()
        # Check for data validity:
        if data is None:
            error(400, "Missing one or more required fields")
        if data.get('first_name') is None:
            error(400, "Missing first name")
        if data.get('last_name') is None:
            error(400, "Missing last name")

        # response = make_response()
        credentials = {'first': data['first_name'], 'last': data['last_name'],
                       'middle': data['middle_name']}
        username, password = Search._oeci_login_params(request)
        # s = requests.Session()
        # s.get()
        verify_credentials = Crawler.attempt_login(username, password)
        # call search method
        search_results = Crawler.search(session, verify_credentials, credentials['first'], credentials['last'],
                                        credentials['middle'])
        return json.dumps(search_results)

    @staticmethod
    def _oeci_login_params(request):
        cipher = DataCipher(key=current_app.config.get("SECRET_KEY"))
        if not "oeci_token" in request.cookies.keys():
            error(401, "Missing login credentials to OECI.")
        decrypted_credentials = cipher.decrypt(request.cookies["oeci_token"])
        return decrypted_credentials["oeci_username"], decrypted_credentials["oeci_password"]


def register(app):
    app.add_url_rule("/search", view_func=Search.as_view("search"))

