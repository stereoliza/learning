import cache
from location import get_response
import sys

ip = str(sys.argv[1])
response = get_response(ip)

try:
    location = cache.get_value(ip)
    if location is None:
        location = cache.set_value(ip, response)
    else:
        print(location)
finally:
    print('Success!')
