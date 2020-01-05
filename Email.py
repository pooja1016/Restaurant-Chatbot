import smtplib
from email.message import EmailMessage

def send_mail(mailId, mailBody):
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login('restaurant.chatbot.help@gmail.com', 'Restaurants12#')
		msg = EmailMessage()
		msg.set_content(mailBody)
		msg['Subject'] = 'Top 10 restaurants'
		msg['From'] = 'restaurant.chatbot.help@gmail.com'
		msg['To'] = mailId
		server.sendmail('restaurant.chatbot.help@gmail.com',[mailId, "bhathaluri.pooja@gmail.com"],msg.as_string())
	except Exception as e:
		return(str(e))    
