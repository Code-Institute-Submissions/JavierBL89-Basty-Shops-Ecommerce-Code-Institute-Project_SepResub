from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_subs_confirm_email(new_member):
    """Send the user a confirmation email"""
    print('puta')
    cust_email = new_member.email
    subject = render_to_string(
        'newsletter/subs_confir_email/confirmation_email_subject.txt',
        {'new_member': new_member})
    body = render_to_string(
        'newsletter/subs_confir_email/confirmation_email_body.txt',
        {'new_member': new_member,
         'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
    )
