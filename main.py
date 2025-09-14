from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend URL
origins = [
    "https://demo-weather-ui-1023393735816.us-central1.run.app",
    "http://localhost:3000"  # for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather")
def get_weather(city: str):
    if not OPENWEATHER_API_KEY:
        return {"error": "API key not configured"}
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()
