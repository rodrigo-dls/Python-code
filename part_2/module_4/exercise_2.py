# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests
import json

city_name = input("Enter name of a municipality: ")
units = 'metric'    # metric units to print temperature in Celsius
request = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid=864acf5017b18fd3f074e343f02400ca'

response = requests.get(request).json()

# print(json.dumps(response, indent=2))   # use the indented format to find the desired 'keys'

print(f"""
===== Weather report for {city_name} ===== 
----> {response['weather'][0]['main']} - {response['weather'][0]['description']}
Temperature:
----> {response['main']['temp']} celsius
""")
