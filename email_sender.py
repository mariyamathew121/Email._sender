from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender='mariyamathew@gmail.com'
email_password=password
email_receiver=" wimok24224@carspure.com"

subject="placement training"
body="""
placement training is happenining on tommorrow please join on correct time
"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())




