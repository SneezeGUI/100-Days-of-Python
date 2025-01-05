import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AMADEUS_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_SECRET = os.getenv('AMADEUS_SECRET')
CITY_SEARCH_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
FLIGHT_OFFER_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
OAUTH_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
class FlightSearch:
    def __init__(self):
        self.cities_to_search = {}
        self.token = self.get_new_token()
    def get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_KEY,  # self._api_key,
            'client_secret': AMADEUS_SECRET,  # self._api_secret
        }
        response = requests.post(url=OAUTH_ENDPOINT, headers=header,
                                 data=body)

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    ## SEARCH FOR IATA CODE
    def get_destination_code(self, city):
        ##search AMADEUS for iata codes
        #for city in self.cities_to_search:
        headers = {
            'Authorization':f'Bearer {self.token}'
        }
        body = {
            'keyword':city,
            'max':'2',
            'include':'AIRPORTS'
        }
        response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=headers,params=body)
        code = response.json()["data"][0]['iataCode']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "USD",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_OFFER_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
