import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers= {
    'Content-Type': 'application/json',
    'x-app-id': api_key,
    'x-app-key': secret_key
}

query = input("what do you do today? : ")
data = {
    "query": query,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 175,
    "age": 22
}

nutritionix_response = requests.post(nutritionix_endpoint, headers=headers, json=data)
result = nutritionix_response.json()

today_date = datetime.today().strftime('%Y-%m-%d')
time_now = datetime.today().strftime('%H:%M:%S')
exersice = result["exercises"][0]["name"]
duration_min = result["exercises"][0]["duration_min"]
nf_calories = result["exercises"][0]["nf_calories"]

sheety_endpoint = "https://api.sheety.co/.../workoutTracking/workouts"

sheety_input = {
    "workout":{
        "date":today_date,
        "time":time_now,
        "exercise": exersice,
        "duration":duration_min,
        "calories": nf_calories,
    }
}

sheety_response = requests.post(sheety_endpoint, json=sheety_input)

