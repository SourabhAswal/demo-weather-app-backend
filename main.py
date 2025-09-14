# main.py
from fastapi import FastAPI
import requests
import os

app = FastAPI()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()
