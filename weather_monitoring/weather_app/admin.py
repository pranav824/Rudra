from django.contrib import admin
from .models import WeatherData, DailySummary

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'temp', 'main', 'timestamp')

@admin.register(DailySummary)
class DailySummaryAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'avg_temp', 'max_temp', 'min_temp', 'dominant_condition')
