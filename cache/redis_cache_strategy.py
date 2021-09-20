import redis

redis_client = redis.Redis(host ='localhost', port=6379, db=0)


def get_from_cache_redis(ip):
    location = redis_client.get(ip)
    return location


def set_in_redis(ip, response):
    redis_client.set(ip, response)
    print(response)
