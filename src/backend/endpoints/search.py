from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import requests
from src.backend.crypto import DataCipher
from src.backend.crawler.crawler import Crawler

# Set to True to display time taken to execute search
TIMER = False


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


class Search(MethodView):
    def post(self):
        if TIMER:
            import time
            start_time = time.time()

        data = request.get_json()

        # Check for data validity:
        if data is None:
            error(400, "Missing first and last name")
        if len(data.get('first_name')) == 0:
            error(400, "Missing first name")
        if len(data.get('last_name')) == 0:
            error(400, "Missing last name")

        search_credentials = {'first': data['first_name'],
                              'last': data['last_name'],
                              'middle': data['middle_name']}

        session = requests.Session()

        username, password = Search._oeci_login_params(request)
        verify_login_credentials = Crawler.attempt_login(session, username, password)
        # Call search method
        search_results = Crawler.search(session, verify_login_credentials,
                                        search_credentials['first'],
                                        search_credentials['last'],
                                        search_credentials['middle'])
        if TIMER:
            print("--- Total Time: %s seconds ---" % (time.time() - start_time))

        return json.dumps(search_results)

    @staticmethod
    def _oeci_login_params(request):
        cipher = DataCipher(key=current_app.config.get("SECRET_KEY"))
        if not "oeci_token" in request.cookies.keys():
            error(401, "Missing login credentials to OECI.")
        try:
            decrypted_credentials = cipher.decrypt(request.cookies["oeci_token"])
        except:
            error(401, "Missing login credentials to OECI.")
        return decrypted_credentials["username"], decrypted_credentials["password"]


def register(app):
    app.add_url_rule("/search", view_func=Search.as_view("search"))