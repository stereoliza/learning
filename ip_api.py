import requests

response = requests.get("http://ip-api.com/json/76.170.183.186").json()
print(response)
print(response['regionName'])
print(response['city'])
print(response['lat'])
print(response['lon'])
