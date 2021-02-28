from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify
from src.backend.crawler import Crawler, UnableToReachOECI, InvalidLoginCreds


# log an error message and stop process
def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


class OeciLogin(MethodView):
    def post(self):
        data = request.form
        print(request.cookies)

        response = make_response()
        # Check for data validity:
        if data is None:
            error(400, "Missing one or more required fields")
        if data['oecilogin'] is None:
            error(400, "Missing OECI login username")
        if data['oecipassword'] is None:
            error(400, "Missing OECI login password")

        credentials = {'username': data['oecilogin'], 'password': data['oecipassword']}

        # Try to log into OECI database
        try:
            Crawler.attempt_login(credentials['username'], credentials['password'])
        except UnableToReachOECI:
            error(404, "Unable to reach OECI database")
        except InvalidLoginCreds:
            error(401, "Invalid login credentials")

        response.set_cookie("test", "success")
        return response, 201


def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
