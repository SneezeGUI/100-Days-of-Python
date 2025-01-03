import requests
from datetime import datetime
import os
APP_ID = os.getenv('NUTRI_APP_ID')
API_KEY = os.getenv('NUTRI_API_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT') # replace with your Sheety API Endpoint
SHEETY_BEARER_TOKEN = os.getenv('SHEETY_BEARER_TOKEN')
GENDER = 'male'
WEIGHT_KG = 187
HEIGHT_CM = 185.42
AGE = 23
exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text =input("Tell me which exercises you did: ")
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime("%X")
print(date)
headers={     "x-app-id": APP_ID,      "x-app-key": API_KEY, }
parameters={     "query": exercise_text, # dummy query for testing purposes
                  "gender": GENDER,
                  "weight_kg": WEIGHT_KG,
                  "height_cm": HEIGHT_CM,
                  "age": AGE}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)  # Send POST request to Nutritionix API with parameters and headers
if response.status_code == 200:  # This is checking if HTTP status code 200 means OK
    result = response.json() # Parse the JSON data into Python object for easy access
    exercises = result['exercises']
    print(result)
    print(exercises)
else:
    print(f"Failed to get exercises data, got error {response.status_code}")
for exercise in result["exercises"]:
    headers = {'Authorization': SHEETY_BEARER_TOKEN}
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEETY_ENDPOINT, headers=headers, json=sheet_inputs)
    print(sheet_response.text)