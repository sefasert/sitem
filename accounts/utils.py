from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_notif(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(mail_template, context)
    to_email = context["user"].email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
