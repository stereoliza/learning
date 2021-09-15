import redis, json
from get_url import get_response
from get_ip import ip


def cache_in_redis():
    redis_client = redis.Redis(host ='localhost', port=6379, db=0)

    address = redis_client.get("city")
    if address is None:
        response = get_response
        redis_client.set("city", str(response['city']))

    address = redis_client.get(ip)
    print(address)