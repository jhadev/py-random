# import requests module

import requests
import config
from pprint import pprint

url = "https://api.yelp.com/v3/businesses/search"

headers = {"Authorization": "Bearer " + config.key}
params = {"location": "NYC", "term": "Pizzeria"}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

top_rated = [
    business["name"] for business in businesses if business["rating"] > 4
]

print(top_rated)
# for business in businesses:
#     print(business["name"])
