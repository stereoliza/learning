import redis

redis_client = redis.Redis(host ='localhost', port=6379, db=0)


def get_from_cache_redis(key):
    location = redis_client.get(key)
    return location


def set_in_redis(key, response):
    redis_client.set(key, response)
    print(response)
