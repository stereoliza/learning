import requests
import os
import sys

response = None
try:
    response = open('response.txt', 'r')
    s = os.stat('response.txt')
    if s.st_size > 0:
        location = response.read()  
    elif s.st_size == 0:
        response = open('response.txt','a')
        location = requests.get("http://api.positionstack.com/v1/reverse",
                            params = {'access_key': 'f937cc4d1db8c3bff099546054e7ab0d',
                                  'query': '33.8755584,-118.3121408'}).json()
        response.write(str(location))
        print(location)
finally:
    if response:
        response.close()
