from django.test import TestCase
from .models import WeatherData

class WeatherDataTestCase(TestCase):
    def test_temperature_conversion(self):
        kelvin_temp = 300  # Example temperature in Kelvin
        celsius_temp = kelvin_temp - 273.15
        self.assertEqual(celsius_temp, 26.85)

    def test_weather_data_creation(self):
        weather = WeatherData.objects.create(
            city="Delhi",
            main="Clear",
            temp=28.5,
            feels_like=30.0,
            timestamp="2024-10-17 12:00:00"
        )
        self.assertEqual(str(weather), "Delhi - 2024-10-17 12:00:00")
