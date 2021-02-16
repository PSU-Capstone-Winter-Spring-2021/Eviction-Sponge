from flask.views import MethodView
from flask import request, make_response, current_app



class OeciLogin(MethodView):
    def post(self):
        data = request.form
        print(data)
        # Check for data validity:
        #if data is None or data[0] is None or data[1] is None:
            #current_app.logger.error("400: Missing one or more required fields")
        #credentials = {"oeci_username": data["oecilogin"], "oeci_password": data["oecipassword"]}
        # TODO: login
        #print(credentials)

        response = make_response()
        return response, 201



def register(app):
    app.add_url_rule("/login", view_func=OeciLogin.as_view("login"))
