import cache
from location import get_response
import sys

ip = str(sys.argv[1])
response = get_response(ip)
cache.get_value(ip, response)
