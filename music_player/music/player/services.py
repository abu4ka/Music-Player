import requests

def get_music(query):
    url = f'https://api.deezer.com/search?q={query}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
