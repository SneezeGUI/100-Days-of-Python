import requests
import json
import os

#D7 API
SMS_API_KEY = os.environ.get('D7_API_KEY')
print(SMS_API_KEY)
url = "https://api.d7networks.com/messages/v1/send"

payload = json.dumps({
  "messages": [
    {
      "channel": "sms",
      "recipients": [
        "+12069541504"
      ],
      "content": "It's going to rain today, dress accordingly. (⊙＿⊙') ",
      "msg_type": "text",
      "data_coding": "text"
    }
  ],
  "message_globals": {
    "originator": "SignOTP",
    "report_url": "https://the_url_to_recieve_delivery_report.com"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer {SMS_API_KEY}'
}
#END D7 API SETUP

# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.environ.get('OWM_API_KEY')
print(API_KEY)
MY_LAT = 47.75448
MY_LONG = -121.91477
parameters = {
    'lat':MY_LAT,
    'lon':MY_LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(url=OWM_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
forecast_list = data['list']

will_rain = False
for entry in forecast_list:
     weather = (entry['weather'])
     for item in weather:
         if item['id'] < 700:
             will_rain=True
if will_rain:
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    # print('it gon rain bitch')
