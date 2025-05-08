import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "location": "NYC",
    "term": "Barber"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
highlyRated = [business["name"]
               for business in businesses if business["rating"] > 4.5]

print(highlyRated)
