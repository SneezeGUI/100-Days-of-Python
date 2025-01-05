import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self.bearer = os.environ["SHEETY_BEARER"]
        self.headers = {
            'Authorization': f"Bearer {self.bearer}",
        }
        self.destination_data = {}
        self.users_endpoint = os.getenv('SHEETY_USERS_ENDPOINT')
        self.prices_endpoint= os.getenv('SHEETY_PRICES_ENDPOINT')
        self.user_emails = []
    def get_user_emails(self):
        response = requests.get(url=self.users_endpoint, headers=self.headers)
        data = response.json()
        for user in data['users']:
            email = user['email']
            self.user_emails.append(email)
        return self.user_emails
    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.prices_endpoint,headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self,):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                headers= self.headers,
                json=new_data
            )
            print(response.text)

