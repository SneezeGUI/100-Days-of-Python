import requests
from datetime import datetime
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# iss_position = (longitude,latitude)
#
# print(iss_position)
MY_LAT = #latitide
MY_LONG = #longitude
MY_TZID = 'America/Los_Angeles'

time_now = datetime.now()

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'tzid': MY_TZID,
    'formatted': 0
}
#https://api.sunrise-sunset.org/json?lat=47.75448&lng=-121.91477&tzid=America/Los_Angeles
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
##GET SUNRISE HOUR FROM REQUEST
# sunrise_split_1 = sunrise.split('T')
# sunrise_split_2 = sunrise_split_1[1].split(':')
# sunrise_hour = sunrise_split_2[0]
# sun = sunrise.split('T')[1].split(':')[0]
##
if sunrise_hour == time_now.hour:
    print('WAKEUP')


print(data)
print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)