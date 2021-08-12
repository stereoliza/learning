import requests
import redis, json

redis_client = redis.Redis(host ='localhost', port=6379, db=0)

response = redis_client.get('response')
if response is None:
    response = requests.get("http://api.positionstack.com/v1/reverse",
                        params = {'access_key': 'f937cc4d1db8c3bff099546054e7ab0d',
                                  'query': '33.8755584,-118.3121408'}).json()
    redis_client.set('response', json.dumps(response))
else:
    response = json.loads(response)


print(response)
