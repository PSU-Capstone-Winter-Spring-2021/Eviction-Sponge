from flask.views import MethodView
from flask import request, make_response, current_app, abort, jsonify, json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def main():
    #This works to send an email but requires the password to be hard coded..

    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''
    #The mail addresses and password
    sender_address = 'sender@gmail.com'
    sender_pass = 'password'
    receiver_address = 'receiver@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

if __name__ == "__main__":
    main()