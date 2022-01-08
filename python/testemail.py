from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#import email
message = MIMEMultipart()
message["from"] = "Niyi"
message["to"] = "otniy@yahoo.com"
message["subject"] = "This is test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
 smtp.ehlo()
 smtp.starttls()
 smtp.login("niyoto@gmail.com","niyoto87")
 smtp.send_message(message)
print("sent")