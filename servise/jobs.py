import os
from datetime import datetime
import pytz
import smtplib
from django.conf import settings
from django.core.mail import send_mail

from servise.models import MailSettings, Log, Client

def send_email(ms, cl, ml, tz):
    try:
        send_mail(ms.title, ms.body, settings.EMAIL_HOST_USER, [cl.email])
        log = Log.objects.create(user=cl, mail=ms.id, last_try_date=datetime.now(tz), server_response='Успешно', try_status='200')
        log.save()
    except smtplib.SMTPException as err:
        log = Log.objects.create(user=cl, mail=ml, last_try_date=datetime.now(tz), server_response='Ошибка', try_status=err)
        log.save()

def test_job(aaa):
    mails = MailSettings.objects.filter(mailing_status='s')
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(tz)
    import pdb; pdb.set_trace()
    for mail in mails:
        for client in mail.clients.all():
            ml = Log.objects.filter(user=client,  mail=mail)
            if ml.exists():
                last_try_date = ml.order_by('-last_try_date').first()
                diff = (now - last_try_date).days
                if mail.mailing_periodicity == "d" and diff >= 1:
                    send_email(mail, client)
                if mail.mailing_periodicity == "w" and diff >= 7:
                    send_email(mail, client)
                if mail.mailing_periodicity == "m" and diff >= 30:
                    send_email(mail, client)
            else:
                send_email(mail, client, ml, tz)  


