import requests
from twilio.rest import Client
import os

# paste your (open weather map) api_key, auth_token, account_sid, here i just hided my details using environmental variables
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")

OWM_endpoind = "https://api.openweathermap.org/data/2.5/forecast"
# paste you open weather map account sid

from_number = "paste your twilio account generated number"
to_number = "paste your personal mobile number (Ex: '+91123456789')"
parameters = {
    # put you place co-ordinates
    "lat" : 0, # lattitude 
    "lon" : 0, # longitude
    "appid": api_key,
}
response = requests.get(url=OWM_endpoind, params=parameters)
weather_data = response.json()

will_it_rain = False

for i in range(4):
    hour_data = weather_data["list"][i]
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_it_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, Remember to carry an ☔️",
            from_=from_number,
            to=to_number,
        )
    print(message.status)



