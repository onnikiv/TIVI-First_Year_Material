# Moduuli 12 esimerkit

import requests


def search_shows(search_query):
    response = requests.get(f'http://api.tvmaze.com/search/shows?q={search_query}')
    shows = response.json()
    # print(f"Ensimmäinen sarja: {shows[0]['show']['name']}")
    # Tulostetaan kaikki hakutulokset.
    print(f"\nHaun tulokset hakusanalla: {search_query}")
    for show in shows:
        # haetaan genret sisäkkäisellä silmukalla
        genres = ""
        for genre in show['show']['genres']:
            genres += genre + genre
        print(f"Sarjan nimi:    {show['show']['name']} ({genres}): {show['show']['url']}")


search_input = input("Anna hakusana:\n")
search_shows(search_input)