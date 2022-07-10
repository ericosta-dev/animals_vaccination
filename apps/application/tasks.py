from tkinter import X
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import VaccineApplication
from datetime import date



@shared_task(name='send_mail')
def add():
    today = date.today()
    TITLE = 'Notificação de Vacinação'
    
    daily_mails = VaccineApplication.objects.filter(
        active=True,
        notify_date=today,
        sent=False)

    if daily_mails.exists():
        for mail in daily_mails:
            user = mail.application.user.username
            email = mail.application.user.email
            animal = mail.application.animal.name
            day = today.strftime("%d/%m/%Y")
            vaccine = mail.vaccine.name

            MAIL_BODY= f'''
            Olá, {user}!
            Informamos que no próximo dia {day}, o seu pet {animal} terá que aplicar vacina {vaccine}!
            Atenciosamente,
            Sistema de Controle Digital de Vacinação
            '''
            sent_mail = True   

            try:
                send_mail(
                    TITLE,
                    MAIL_BODY,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                sent_mail = False
                print(e)

            
            if sent_mail:
                mail.sent = True
                mail.save()
