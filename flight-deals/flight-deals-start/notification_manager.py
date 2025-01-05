import os
import requests
import smtplib

from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.contact = '2069541504'
        self.key = os.getenv('TEXTBELT_API')
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = os.getenv('SMTP_PORT')
        self.smtp_email = os.getenv('SMTP_EMAIL')
        self.smtp_pass = os.getenv('SMTP_PASSWORD')

    def send_email(self, recipients, message):
        for recipient in recipients:
            with smtplib.SMTP(host=self.smtp_server, port=int(self.smtp_port)) as connection:
                connection.starttls()
                connection.login(user=self.smtp_email, password=self.smtp_pass)
                connection.sendmail(
                    from_addr=self.smtp_email,
                    to_addrs=recipient,
                    msg=f'{message}')
        print('Emails Sent.')

    def notify(self, message):
        resp = requests.post('https://textbelt.com/text',{
            'phone': self.contact,
            'message': message,
            'key': self.key,
        })
        print(resp.json())