#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_sender = 'sashanowoe1@gmail.com'
mail_receiver = ['test1@gmail.com', 'test2@gmail.com']

username = 'sashanowoe1@gmail.com'
password = '***********'
server = smtplib.SMTP('smtp.gmail.com', 587)

subject = u'Test email.'
body = u'Hi. This sending email by python'
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(mail_sender, mail_receiver, msg.as_string())
server.quit()
