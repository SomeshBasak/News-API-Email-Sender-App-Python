import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "saaarkb16@gmail.com"
    password = "wrnenkuvnpcicmsj"

    receiver = "someshbasak2016@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)