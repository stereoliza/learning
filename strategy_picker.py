import get_url
import mysql_cache_strategy
import redis_cache_strategy
import file_cache_strategy


def get_location():
    try:
        mysql_cache_strategy.cache_in_mysql()
    except:
        try:
            redis_cache_strategy.cache_in_redis()
        except:
            file_cache_strategy.cache_in_file()
    finally:
        print("Success")