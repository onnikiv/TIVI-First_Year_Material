import json
import requests

user_input = input("Anna paikkakunnan nimi:\n")

pyyntö = "http://api.openweathermap.org/data/2.5/weather?q=" + user_input + "&appid=APIKEY&units=metric"