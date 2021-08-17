import requests

response = None
try:
    response = open('response.txt', 'w+')
    location = response.read()
    if location !='':
        location = response.read()
        print(location)
    else:
        response = open('response.txt','w')
        location = requests.get("http://api.positionstack.com/v1/reverse",
                        params = {'access_key': 'f937cc4d1db8c3bff099546054e7ab0d',
                                  'query': '33.8755584,-118.3121408'}).json()
        response.write(str(location))
        print(location)
finally:
    if response:
        response.close()
