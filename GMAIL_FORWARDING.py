#!/usr/bin/python
#only for extracting non-html email and automatically forward it.
import smtplib,imaplib,email


def sendmail(textforsending,passwd):
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	email='from_mail@gmail.com'
	s.login(email,passwd)
	toemail='to_mail@gmail.com'
	s.sendmail(email,toemail,textforsending)
	s.quit()
	


def imapobj():
	imapobj=imaplib.IMAP4_SSL('imap.gmail.com')
	passwd=input('enter password')
	imapobj.login('from_mail@gmail.com',passwd)
	return imapobj


def modify(data):
	data=str(data)
	i=(data.split())
	i[0]=i[0][3:]
	i[len(i)-1]=i[len(i)-1][:-2]
	return i


imapobj=imapobj()

imapobj.select('"[Gmail]/All Mail"')
result,data=imapobj.uid('search',None,"UNSEEN")
if result=='OK':
	data=modify(data)
	if data!=['']:
		for qw in range(len(data)):
			result,message_data=imapobj.uid('fetch',data[qw],'RFC822')
			if result=='OK':
				email_data=email.message_from_bytes(message_data[0][1])
				raw_email_string=message_data[0][1].decode('utf-8')
				email_message=email.message_from_string(raw_email_string)
				for part in email_message.walk():
					if part.get_content_type() == 'text/plain':
						body=part.get_payload(decode=True)
						print(body.decode('utf-8'))
						sendmail(body.decode('utf-8'),input('enter password'))
	else:
		print('No UNSEEN EMAIL')

imapobj.logout()
