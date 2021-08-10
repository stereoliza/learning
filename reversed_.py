import requests

response = requests.get("http://api.positionstack.com/v1/reverse",
                        params = {'access_key': 'f937cc4d1db8c3bff099546054e7ab0d',
                                  'query': '33.8755584,-118.3121408'}).json()
print(response)
