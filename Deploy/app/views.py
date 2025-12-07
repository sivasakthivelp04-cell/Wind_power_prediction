import requests
from django.shortcuts import render, redirect
import numpy as np
import joblib

model = joblib.load('D:/Final_Year_Project/8th Sem Project/Gdrive/Deploy/app/deploy.pkl')

# OpenWeather API Key
API_KEY = '51ba97a538c7fefc33fefeccf5863719'

# Home Page
def home(request):
    return render(request, "index.html")

# Predict Wind Power
def predict(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()][1:]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = prediction[0]
        return render(request, 'index.html', {"prediction_text": f'{output}kw'})

# Check Weather Conditions
def check_weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                "city": city,
                "wind_speed": response['wind']['speed'],
                "wind_direction": response['wind']['deg'],
                "pressure": response['main']['pressure'] / 1013.25,  # Convert to atm
                "temperature": response['main']['temp']
            }
            return render(request, 'index.html', {"weather_data": weather_data})
        else:
            return render(request, 'index.html', {"weather_error": "Unable to fetch weather data. Please try again."})
