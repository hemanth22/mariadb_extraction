# import the necessary components first
import smtplib
import mimetypes
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

port=465
smtp_server = os.environ.get("SMTP_ADDRESS")
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
sender_email = "hemanth22hemu@gmail.com "
receiver_email = "hemanthbitra@live.com"
filename = "test.csv"
message = MIMEMultipart("alternative")
message["Subject"] = "[High] mariadb_extraction status"
message["From"] = sender_email
message["To"] = receiver_email

message.attach(MIMEText(file("test.csv").read()))

# write the plain text part
text = """\
|INFORMATION|

mariadb_extraction job completed now.

Thanks,
Information Mangement."""
# write the HTML part
html = """\
<html>
  <body>
<h1 style="text-align: center;"><span style="color: #ff0000;"><strong>|INFORMATION|</strong></span></h1>
<h3 style="text-align: center;">mariadb_extraction job completed now.</h3>
<p style="text-align: center;"><strong>Thanks,</strong></p>
<p style="text-align: center;"><strong>Information Mangement.</strong></p>
  </body>
</html>
"""
# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
# send your email
with smtplib.SMTP_SSL(smtp_server,port) as mailserver:
    mailserver.login(USER_EMAIL,USER_PASSWORD)
    mailserver.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Sent')
