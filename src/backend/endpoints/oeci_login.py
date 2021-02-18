from flask.views import MethodView
from flask import request, make_response, current_app



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
        print(credentials)
        response.set_cookie("test", "success")

        # TODO: pass login info to crawler to start process

        return response, 201



def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
