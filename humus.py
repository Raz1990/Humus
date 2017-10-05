import sys
from pyquery import PyQuery as pq
import urllib
import smtplib

site = sys.argv[1]
search_word = sys.argv[2]
mail_to = sys.argv[3]

print(search_word)

d = pq(url=site)

#if file doesn't exist, create it. Otherwise, open it for both read/write
f = open('site', 'a+')

#get curser to the beginning, so it could be read from start to end.
f.seek(0)
text = f.read()

#no further use for the file for now
f.close()

#search the entire body of the HTML for the keyword
found = d('body:contains('+search_word+')').text()

if (found != text):
#if found new content in HTML, overwrite the existing text file with a new one containing all of the new informtaion
	with open('site','w') as f:
		f.write(found)
# Email.
	gmail_user = 'WebsiteChangeDetector.R@gmail.com'  
	gmail_password = '123passwor'
	sent_from = gmail_user  
	to = mail_to
	subject = 'New changes found in ' + site  
	body = found
	email_text = """\  
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)
	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()
	except:
		print("Unexpected error")
