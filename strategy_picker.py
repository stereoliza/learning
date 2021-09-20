import cache.mysql_cache_strategy
import cache.redis_cache_strategy
import cache.file_cache_strategy
from get_url import get_response


def get_location(ip):
    response = get_response(ip)
    try:
        cache.mysql_cache_strategy.open_db()
        location = cache.mysql_cache_strategy.get_from_mysql(ip)
        if location is None:
            print(response)
            cache.mysql_cache_strategy.insert_data(ip, response)
        else:
            print(location)
    except:
        try:
            location = cache.redis_cache_strategy.get_from_cache_redis(ip)
            if location is None:
                cache.redis_cache_strategy.set_in_redis(ip, response)
            else:
                print(location)
        except:
            try:
                location = cache.file_cache_strategy.get_from_file()
                print(location)
                if location == '':
                    cache.file_cache_strategy.write_in_file(response)
                else:
                    print(location)
            finally:
                cache.file_cache_strategy.close()
    finally:
        print("Success")


