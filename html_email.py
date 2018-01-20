#!/usr/bin/env python3  

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


fromaddr = 'from_mail@gmail.com'
toaddr = 'to_mail@gmail.com'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject']='Test email'


body = 'from me to me'
html_text = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""


msg.attach(MIMEText(body,'plain'))
msg.attach(MIMEText(html_text,'html'))

msg_text = msg.as_string()
smtpobj = smtplib.SMTP('smtp.gmail.com',587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()

passwd=input('enter password')
smtpobj.login(fromaddr,passwd)
smtpobj.sendmail(fromaddr,toaddr,msg_text)


smtpobj.quit()
