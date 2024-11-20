import requests
import os
from twilio.rest import Client

account_sid = os.environ['ACCOUNT_ID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)

weather_param = {
    "lat": 9.03,
    "lon": 38.74,
    "appid": "9278810435b1683e5341e99f6086da4d",
    "units": "metric"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weather_param)

response.raise_for_status()
data = response.json()
id = data["weather"][0]["id"]

message = client.messages.create(
    body="Hello!, it's going to rain today, Being with Umbrella ☔️.\nHave A good Day 😊",
    from_="+15017122661",
    to="+251947414175",
)

print(message.status)
