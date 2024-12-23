import requests
import json
import os
import time

TEXTBELT_KEY = os.environ.get('TEXTBELT_API_KEY')
print(TEXTBELT_KEY)
def send_sms():
    # local_sms_server = 'http://127.0.0.1:9090/text',
    contact_1 = requests.post(  'https://textbelt.com/text',
                              {'phone': "5555555555",
                               'message': 'It will probably rain in the next 6 hours... Bring a jacket! 🌧️',
                                'key': TEXTBELT_KEY,
                               })
    # success_state = contact_1.json()['success']
    texbelt_success = contact_1.json()['success']
    textbelt_balance = contact_1.json()['quotaRemaining']

    print(f'TextBelt Success?: {texbelt_success}\nBalance Remaining: {textbelt_balance}')
    # contact_2 = requests.post('http://127.0.0.1:9090/text',
    #                           {'number': "5555555555",
     #                           'message': 'It will probably rain in the next 6 hours... Bring a jacket!',
     #                           })
    # print(f'Local SMS Success: {contact_2.json()['success']}')
    successful= texbelt_success
    if not successful:
        print('Trying again in 120s...')
        time.sleep(120)
        send_sms()

def sleep():
    print('Waiting 6 hours to update again')
    time.sleep(21600)#21600 is 6hr


OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.environ.get('OWM_API_KEY')
print(API_KEY)
MY_LAT = os.environ.get('MY_LATITUDE')
print(MY_LAT)
MY_LONG = os.environ.get('MY_LONGITUDE')
print(MY_LONG)
parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 4,
}
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
forecast_list = data['list']


def check_weather():

    will_rain = False
    for entry in forecast_list:
         weather = (entry['weather'])
         for item in weather:
             print(item['id'])
             if item['id'] < 700:
                 will_rain=True
    if will_rain:
        send_sms()
        sleep()
        check_weather()
check_weather()