import cache_strategy.mysql_cache_strategy
import cache_strategy.redis_cache_strategy
import cache_strategy.file_cache_strategy


def get_value(ip, response):
    try:
        cache_strategy.mysql_cache_strategy.open_db()
        location = cache_strategy.mysql_cache_strategy.get_from_mysql(ip)
        if location is None:
            print(response)
            cache_strategy.mysql_cache_strategy.insert_data(ip, response)
        else:
            print(location)
    except:
        try:
            location = cache_strategy.redis_cache_strategy.get_from_cache_redis(ip)
            if location is None:
                cache_strategy.redis_cache_strategy.set_in_redis(ip, response)
            else:
                print(location)
        except:
            try:
                location = cache_strategy.file_cache_strategy.get_from_file()
                print(location)
                if location == '':
                    cache_strategy.file_cache_strategy.write_in_file(response)
                else:
                    print(location)
            finally:
                cache_strategy.file_cache_strategy.close()
    finally:
        print("Success")
