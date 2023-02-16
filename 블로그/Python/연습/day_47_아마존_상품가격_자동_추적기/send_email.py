import os
import dotenv
import smtplib
from email.mime.text import MIMEText

dotenv.load_dotenv()

class SendEmail:
    def __init__(self):
        self.smtp_url = os.getenv("smtp_url")
        self.smtp_port = os.getenv("smtp_port")
        self.my_email = os.getenv("my_email")
        self.my_password = os.getenv("my_password")

    def send_email(self, receiver, content, subject):
        connection = smtplib.SMTP_SSL(url=self.smtp_url, port=self.smtp_port)
        connection.login(self.my_email, self.my_password)

        msg = MIMEText(content)
        msg["From"] = self.my_email
        msg["Subject"] = subject
        msg["To"] = receiver

        connection.sendmail(self.my_email, receiver, msg.as_string())
        connection.close