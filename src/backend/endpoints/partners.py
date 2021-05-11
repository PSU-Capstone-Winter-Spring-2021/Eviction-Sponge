from flask import json
from flask.views import MethodView
import os


class Partners(MethodView):
    def post(self):
        # Get the path information for the source file:
        path = os.path.relpath('frontend\\src\\data\\partnerData.json', os.path.dirname(__file__))

        input_file = open(path, 'r')
        partner_data = json.load(input_file)
        return partner_data


def register(app):
    app.add_url_rule("/partners", view_func=Partners.as_view("partners"))
