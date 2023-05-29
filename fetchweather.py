import json
from urllib.request import urlopen
#Create user account and obtain API key from https://www.weatherapi.com

url = "http://api.weatherapi.com/v1/current.json?key=e07cf783bb8842669da43922232905&q=London&aqi=no"

api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)

print("Raw Data")
print(json_api)

print("Parsed")
data= json_api['location']
print(data)
