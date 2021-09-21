from cache import get_value
from location import get_response
import sys

ip = str(sys.argv[1])
response = get_response(ip)
get_value(ip, response)
