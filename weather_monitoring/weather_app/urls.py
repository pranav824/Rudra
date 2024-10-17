from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the homepage
    path('fetch-weather/', views.fetch_weather, name='fetch_weather'),
]
