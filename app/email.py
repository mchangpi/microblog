from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context(): # Get the application context
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment) # *unpacks the tuple argument into positional arguments
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email,
            # _get_current_object() extracts the actual application instance from the proxy object
            args=(current_app._get_current_object(), msg)).start()