import smtplib
from email.mime.text import MIMEText
import os
import dotenv

dotenv.load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.my_email = os.getenv("my_email")
        self.my_password = os.getenv("my_password")


    def send_email(self, receiver, content):
        connection = smtplib.SMTP_SSL("smtp.naver.com", port=os.getenv("port"))
        connection.login(self.my_email, self.my_password)

        msg = MIMEText(content)
        msg["From"] = self.my_email
        msg["Subject"] = "항공 특가!"
        msg["To"] = receiver

        connection.sendmail(self.my_email, receiver, msg.as_string())
        connection.close()
