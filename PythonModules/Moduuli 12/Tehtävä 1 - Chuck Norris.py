import requests

def chuck_norris_vitsi():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    vitsi = response.json()
    print(f"\n{vitsi['value']}")

chuck_norris_vitsi()
