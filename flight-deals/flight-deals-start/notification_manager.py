import os
import requests

from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.contact = '2069541504'
        self.key = os.getenv('TEXTBELT_API')

    def notify(self, message):
        resp = requests.post('https://textbelt.com/text',{
            'phone': self.contact,
            'message': message,
            'key': self.key,
        })
        print(resp.json())