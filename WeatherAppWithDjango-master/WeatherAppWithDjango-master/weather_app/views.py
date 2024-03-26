from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.urls import reverse

def index(request):
    kelvin = 273
    api_key = "9d8e82de2d002920b7c3d0d2232ad5b3"
    
    if request.POST:
        city = request.POST["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"        
        response = requests.get(url)
        weather_info = response.json()
        temp = weather_info["main"]["temp"] - kelvin
        temp = round(temp, 2)
        main = weather_info["weather"][0]["main"]
        feels_like = weather_info["main"]["feels_like"] - kelvin
        feels_like = round(feels_like, 2)
        icon_code = weather_info["weather"][0]["icon"]
        icon = f"http://openweathermap.org/img/w/{icon_code}.png"

        weather_dictionary = {"city_name" : city,
                        "city_temp" : temp,
                        "city_main" : main,
                        "city_feelslike" : feels_like,
                        "icon" : icon}
        return render(request, "weather_app/index.html", context=weather_dictionary)
    else:
        return render(request, "weather_app/index.html")
        
