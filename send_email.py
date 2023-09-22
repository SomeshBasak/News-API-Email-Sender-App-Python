import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = ""  # Your email address inside the quote.
    password = ""  # Your password of gmail inside the quote.

    receiver = "" # sender email address inside the quote.
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)