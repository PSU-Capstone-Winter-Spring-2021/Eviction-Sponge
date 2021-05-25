from flask import send_file
from flask.views import MethodView
from pathlib import PurePath


class Partners(MethodView):
    def get(self):
        path = PurePath(__file__).parent.parent / 'data' / 'partnerData.json'
        return send_file(str(path), mimetype='application/json')


def register(app):
    app.add_url_rule("/partners-table", view_func=Partners.as_view("partners-table"))
