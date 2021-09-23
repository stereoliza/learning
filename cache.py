import cache_strategy.mysql_cache_strategy
import cache_strategy.redis_cache_strategy
import cache_strategy.file_cache_strategy


def get_value(ip):
    try:
        cache_strategy.mysql_cache_strategy.open_db()
        location = cache_strategy.mysql_cache_strategy.get_from_mysql(ip)
        return location
    except:
        try:
            location = cache_strategy.redis_cache_strategy.get_from_cache_redis(ip)
        except:
            location = cache_strategy.file_cache_strategy.get_from_file()
    finally:
        return location


def set_value(key, response):
    try:
        cache_strategy.mysql_cache_strategy.insert_data(key, response)
    except:
        try:
            cache_strategy.redis_cache_strategy.set_in_redis(key, response)
        except:
            cache_strategy.file_cache_strategy.write_in_file(response)
