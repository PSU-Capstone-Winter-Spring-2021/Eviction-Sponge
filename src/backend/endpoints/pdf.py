from flask import current_app, abort, make_response, jsonify, request, send_file
from flask.views import MethodView
from pdf_creator import CreatePDF


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))

# We need to add a delete bit later in the close program/restart


class Pdf(MethodView):
    def post(self):
        data = request.get_json()
        # check to see if empty
        if data is None:
            error(400, "No data was sent!")
        pdf_creator = CreatePDF()
        pdf_path = pdf_creator.PDF_filler(data)
        return send_file(pdf_path, as_attachment=True)


def register(app):
    app.add_url_rule("/pdf", view_func=Pdf.as_view("pdf"))
