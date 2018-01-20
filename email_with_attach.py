import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email import encoders
import os
"""
extensions of files that we will send
"""
extension = "jpg"
"""
This function returns a tuple with the files located in the 
current
directory
"""

files = os.listdir()
print(files)
 #this program should be saved in the 
#current directory where your files are.

"""
We check what files have our wished extension
"""

for file in files:
    if extension in file:
        user ="sending@gmail.com" #sending gmail
        recv ="receiving@gmail.com" #receiving gmail
        subject = "Subject" #subject of email message
        message = MIMEMultipart()
        message["From"] = user
        message["To"] = recv
        message["Subject"]= subject
        body = "Files with ." + extension + "extension"
        message.attach(MIMEText(body,"plain"))
        attachment = open(file,"rb")
        part = MIMEBase("application","octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition","attachment"; filename=+ file)
        message.attach(part)
        text = message.as_string()
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,"your gmail pasword") 
        server.sendmail(user,recv,text)
        server.quit()
else:
    pass