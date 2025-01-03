import requests
from datetime import datetime
import os
import json

# Fetch environment variables
try:
    APP_ID = os.getenv('NUTRI_APP_ID')
    API_KEY = os.getenv('NUTRI_API_KEY')
    SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')  # replace with your Sheety API Endpoint
    SHEETY_BEARER_TOKEN = os.getenv('SHEETY_BEARER_TOKEN')
except Exception as e:
    print(f"Error fetching environment variables: {e}")
    exit(1)  # Exit script with error status code

GENDER = 'male'
WEIGHT_KG = 85
HEIGHT_CM = 180
AGE = 23

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime("%X")
print(f'Date: {date}, Time: {time}')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,  # Dummy query for testing purposes
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
try:
    response = requests.post(exercise_endpoint, json=parameters, headers=headers)  # Send POST request to Nutritionix API with parameters and headers
except Exception as e:
    print(f"Error occurred when sending a post request to Nutritionix API: {e}")
    exit(1)  # Exit script with error status code

if response.status_code == 200:  # This is checking if HTTP status code 200 means OK
    result = response.json()  # Parse JSON data into Python object for easy access
else:
    print(f"Failed to get exercises data, got error {response.status_code}")
    exit(1)

headers = {'Authorization': SHEETY_BEARER_TOKEN}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
try:
    sheet_response = requests.post(SHEETY_ENDPOINT, headers=headers, json=sheet_inputs)  # Send POST request to Sheety API with parameters and headers
except Exception as e:
    print(f"Error occurred when sending a post request to Sheety API for exercise data: {e}")
    exit(1)  # Exit script with error status code

try:
    print(json.dumps(sheet_response.json(), indent=4))
except Exception as e:
    print(f"Error occurred when converting response json to string: {e}")
