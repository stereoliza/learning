from cache_picker import CacheService
from response import get_response
import ipaddress


def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print('Please, enter valid IP address')
        raise ValueError
    else:
        return True


def find_location(ip):
    finder = CacheService()
    if validate_ip_address(ip) is True:
        location = finder.get_value(ip)
        if location is None:
            location = get_response(ip)
            print(location)
            finder.set_value(ip, location)
        else:
            return location
        return location
