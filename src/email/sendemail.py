import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
#from emailconstuctor import html
from email_subjects import subjects


ht = open('./sample.html')

load_dotenv()
EMAIL_ADD = os.environ.get('EMAIL_ADD')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Hello World'
msg['From'] = 'Drs Reports'
msg['To'] = subjects
msg.set_content('Hello World')
msg.add_alternative(ht.read(), subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user=EMAIL_ADD, password=EMAIL_PASS)
    smtp.send_message(msg)
    print('Message send!')
