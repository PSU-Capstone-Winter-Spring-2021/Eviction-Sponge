from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import requests

def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))

class PartnersPage(MethodView):
    def post(self):

        data = request.get_json()
        if data is None:
            error(400, "Missing one or more required fields")



def register(app):
    app.add_url_rule("/partners?", view_func=PartnersPage.as_view("partners?"))