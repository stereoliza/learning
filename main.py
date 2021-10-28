from cache_picker import CacheService
from location import get_response
import sys

ip = str(sys.argv[1])


def find_location(ip):
    try:
        finder = CacheService()
        location = finder.get_value(ip)
        if location is None:
            response = get_response(ip)
            finder.set_value(ip, response)
        else:
            print(location)
    finally:
        print('Success!')


find_location(ip)
