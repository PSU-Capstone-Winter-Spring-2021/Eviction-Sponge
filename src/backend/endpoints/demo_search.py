import csv
import os
from datetime import datetime

from flask.views import MethodView
from flask import make_response, current_app, abort, jsonify, json
import eligibility_eval
import requests


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


def split_judgements_string(judgements):
    return judgements.split(', ')


#  Made this a function for ease of testing, since patching strptime is a huge hassle for some reason
def string_to_date(string, format):
    return datetime.strptime(string, format).date()


# This class serves to demonstrate the website without concern about displaying real eviction cases
# From an outside perspective, it functions the same as the search endpoint, but the data is made up
class DemoSearch(MethodView):
    def post(self):
        search_results = []
        path = os.path.relpath('backend\\data\\demo_search_data.csv', os.path.dirname(__file__))
        with open(path, newline='\n') as demoFile:
            demoData = csv.reader(demoFile, delimiter=';')
            for fakeCase in demoData:
                eligibility = eligibility_eval.is_eligible(fakeCase[4],
                                                           string_to_date(fakeCase[6], '%m/%d/%Y'),
                                                           split_judgements_string(fakeCase[7]))
                key = fakeCase[0]
                value = {'style': fakeCase[1], 'location': fakeCase[2], 'violation_type': fakeCase[3],
                         'status': fakeCase[4], 'complaint_date': fakeCase[5], 'closed_date': fakeCase[6], 'judgements': split_judgements_string(fakeCase[7]),
                         'eligibility': [True if fakeCase[8] == "True" else False, fakeCase[9]], 'case_id' : fakeCase[10], 'balance': fakeCase[11]}
                search_results.append({key: value})

        # To view all search results:
        # for key, value in search_results.items():
        #     print(key, " : ", value)

        return json.dumps(search_results)


def register(app):
    app.add_url_rule("/demo", view_func=DemoSearch.as_view("demo"))
