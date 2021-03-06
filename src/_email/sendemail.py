import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from .emailconstuctor import gen_email
from .email_subjects import subjects




def sendemail():

    gen_email()

    ht = open('./_email/temp_files/email.html')

    load_dotenv()
    EMAIL_ADD = os.environ.get('EMAIL_ADD')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = 'DRS Reports'
    msg['From'] = 'Drs Reports | Design e Comunicação'
    msg['To'] = subjects
    msg.set_content('DRS Reports')
    msg.add_alternative(ht.read(), subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user=EMAIL_ADD, password=EMAIL_PASS)
        smtp.send_message(msg)
        print(f'Email send to: {subjects}')
