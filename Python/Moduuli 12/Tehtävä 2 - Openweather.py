import json
import requests

APIKEY = ""

def weather():
    paikkakunta_syote = input("Anna paikkakunnan nimi:\n").capitalize()
    paikkakunta = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta_syote}&appid={APIKEY}"
    try: 
        vastaus = requests.get(paikkakunta)
        print(f"HTTP response status code: {vastaus.status_code}")
        saatila = vastaus.json()

        if vastaus.status_code == 200:
            print("\n")
            print(f"Haku: {paikkakunta_syote}")
            print(f"Säätila: {saatila['weather'][0]['description']}")
            print(f"Lämpötila: {saatila['main']['temp'] - 273.15:.2f} °C")

    except requests.exceptions.RequestException as error:
        print("HTTP-pyynnössä tapahtui virhe. Ei verkkoyhteyttä palvelimeen.")
        print(f"Virheilmoitus: {error}")
    
weather()