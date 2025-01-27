# Moduuli 12 esimerkit
import json
import requests


def search_shows(search_query):
    url = f'https://api.tvmaze.com/search/shows?q={search_query}'
    try: 
        response = requests.get(url)
        
        print(f"HTTP response status code: {response.status_code}")
        shows = response.json()
        # print(f"Ensimmäinen sarja: {shows[0]['show']['name']}")
        # Tulostetaan kaikki hakutulokset, jos HTTP-pyyntö onnistui
        if response.status_code == 200:
            print(f"\nHaun tulokset hakusanalla: {search_query}")
            for show in shows:
                # haetaan genret sisäkkäisellä silmukalla
                genres = ""
                for genre in show['show']['genres']:
                    genres += genres + genre + " "
                print(f"Sarjan nimi:    {show['show']['name']} ({genres}): {show['show']['url']}")
            print("\n")

    except requests.exceptions.RequestException as error:
        print("HTTP-pyynnössä tapahtui virhe. Ei verkkoyhteyttä palvelimeen.")
        print(f"Virheilmoitus: {error}")
    



search_input = input("Anna hakusana:\n")
search_shows(search_input)
