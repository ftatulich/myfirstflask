from flask_mail import Message
from flask import render_template
import app
from app import mail, app
from threading import Thread


def send_async_message(app, msg):
    with app.app_context():
        mail.send(msg)


def send_message(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_message, args=(app, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_message(
        "[Microblog] reset your password",
        sender=app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                                  user=user,
                                  token=token
                                  ),
        html_body=render_template("email/reset_password.html",
                                  user=user,
                                  token=token
                                  )
    )
