from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context(): # Get the application context
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # _get_current_object() extracts the actual application instance from the proxy object
    Thread(target=send_async_email, args=(current_app, msg)).start()
