from flask import abort, current_app, jsonify, make_response, request, send_file
from flask.views import MethodView
from src.backend.pdf_creator import CreatePDF


def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))


class Pdf(MethodView):
    def post(self):
        data = request.get_json()
        if data is None:
            error(400, "No data was sent!")
        pdf_creator = CreatePDF()
        pdf, filename = pdf_creator.PDF_filler(data)
        return send_file(pdf, attachment_filename=filename, as_attachment=True)


def register(app):
    app.add_url_rule("/pdf", view_func=Pdf.as_view("pdf"))
