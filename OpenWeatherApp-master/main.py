import requests
import json

kelvin = 273
api_key = "9d8e82de2d002920b7c3d0d2232ad5b3"

city_name = input("Please write a city: ")
city_name = city_name.capitalize()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}"

response = requests.get(url)
weather_info = response.json()

temp = weather_info["main"]["temp"] - kelvin
main = weather_info["weather"][0]["main"]
feels_like = weather_info["main"]["feels_like"] - kelvin

print(f"Weather in {city_name}:\n"
      f"temperature: {format(temp, '.2f')}"
      f" celcius \nmain: {main} \n"
      f"feels_like: {format(feels_like, '.2f')}")