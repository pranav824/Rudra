import requests
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from .models import WeatherData

# Function to fetch weather data for a city
def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    # Convert temperature from Kelvin to Celsius
    temp_celsius = data['main']['temp'] - 273.15
    feels_like_celsius = data['main']['feels_like'] - 273.15

    # Store weather data in the database
    WeatherData.objects.create(
        city=city,
        main=data['weather'][0]['main'],
        temp=temp_celsius,
        feels_like=feels_like_celsius,
        timestamp=timezone.now()
    )

# View for rendering the homepage
def index(request):
    # Fetch recent weather data to display on the homepage
    weather_data = WeatherData.objects.order_by('-timestamp')[:10]
    return render(request, 'weather_app/index.html', {'weather_data': weather_data})

# View for fetching weather data from the API for multiple cities
def fetch_weather(request):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        get_weather_data(city)
    return JsonResponse({'status': 'Data fetched successfully'})
