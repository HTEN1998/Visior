import requests
from pprint import pprint

r = requests.get("https://graphhopper.com/api/1/route?point=19.185206, 72.975723&point=19.179911, 72.980190&vehicle=foot&locale=en&calc_points=true&key=bb5794b7-0b67-401c-834c-81aee1a1302d")

pprint(r.json())

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=4)
