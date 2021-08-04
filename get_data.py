import requests
import json
import re


def get_results(letter: str):

    # Get the end point data
    url = 'https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22'
    response = requests.get(url)
    response_json = response.json()

    count = 0
    cities = []

    if re.match(r'^[a-zA-Z]$', letter):
        for city in response_json['list']:
            city_name = city['name']
            if city_name.startswith(letter) or city_name.startswith(letter.upper()):
                count += 1
                cities.append(city_name)
            all_cities = ', '.join(cities) + '.'
        if count == 0:
            all_cities = f"No city found with the letter '{letter}'."
    else:
        all_cities = "Please enter only an alphabet!"

    return (count, all_cities)
