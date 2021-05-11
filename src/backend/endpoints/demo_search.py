import csv
import os

from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import requests


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


def split_judgements_string(judgements):
    return judgements.split(', ')


# This class serves to demonstrate the website without concern about displaying real eviction cases
# From an outside perspective, it functions the same as the search endpoint, but the data is made up
class DemoSearch(MethodView):
    def post(self):
        data = request.get_json()
        # Check for data validity:
        if data is None:
            error(400, "Missing one or more required fields")
        if data.get('first_name') is None:
            error(400, "Missing first name")
        if data.get('last_name') is None:
            error(400, "Missing last name")

        search_results = {}
        path = os.path.relpath('backend\\data\\demo_search_data.csv', os.path.dirname(__file__))
        with open(path, newline='\n') as demoFile:
            demoData = csv.reader(demoFile, delimiter=';')
            for fakeCase in demoData:
                # file format:
                #   case #, style, location, type, status, closed date, judgements, eligibility T/F, eligibility string
                key = fakeCase[0]
                value = {'style': fakeCase[1], 'location': fakeCase[2], 'violation_type': fakeCase[3],
                         'status': fakeCase[4], 'date': fakeCase[5], 'judgements': split_judgements_string(fakeCase[6]),
                         'eligibility': (fakeCase[7], fakeCase[8])}
                search_results.update({key: value})

        # To view all search results:
        for key, value in search_results.items():
            print(key, " : ", value)

        return json.dumps(search_results)


def register(app):
    app.add_url_rule("/demo", view_func=DemoSearch.as_view("demo"))
