from flask import current_app, abort, make_response, jsonify, request
from flask.views import MethodView
from src.backend.pdf_creator import CreatePDF


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))

# This returns the absolute path of the created pdf. We need to add a delete bit later in the close program/restart


class Pdf(MethodView):
    def post(self):
        data = request.get_json()
        # check to see if empty
        if data is None:
            error(400, "No data was sent!")
        return CreatePDF.PDF_filler(self, data)


def register(app):
    app.add_url_rule("/pdf", view_func=CreatePDF.as_view("pdf"))
