from requests import get
import config

api_key = config.api_key

url = "https://api.yelp.com/v3/businesses/search"

header = {
    "Authorization": "Bearer "+ api_key
}

params = {
    "term": "banks",
    "location": "London"
}
response = get(url, headers=header, params=params)
result = response.json()["businesses"]
#using list comprehension instead of the ordinary for loop afterwards
key = [business["name"] for business in result if business["rating"] > 4.5]
print(key)

#for business in result:
#    print(business["name"], business["url"])