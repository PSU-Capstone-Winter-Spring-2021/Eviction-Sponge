from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import smtplib

def error(code, message):
    current_app.logger.error("code %i %s" % (code, message), stack_info=True)
    return abort(make_response(jsonify(message=message), code))

class PartnersPage(MethodView):
    def post(self):

        data = request.get_json()
        if data is None:
            error(400, "Missing one or more required fields")

        sender = 'from@fromdomain.com'
        receivers = ['to@domain.com']

        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)
            print
            "Successfully sent email"
        except smtplib.SMTPException:
            print
            "Error: unable to send email"

def main():
    sender = 'from@fromdomain.com'
    receivers = ['to@domain.com']

    message = """From: From Person <from@fromdomain.com>
            To: To Person <to@todomain.com>
            Subject: SMTP e-mail test

            This is a test e-mail message.
            """

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print
        "Successfully sent email"
    except smtplib.SMTPException:
        print
        "Error: unable to send email"

if __name__ == "__main__":
    main()

def register(app):
    app.add_url_rule("/partners?", view_func=PartnersPage.as_view("partners?"))