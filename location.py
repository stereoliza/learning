import requests


def get_response(ip):
    url = "http://ip-api.com/json/"
    ip_url = url + ip
    get_url = requests.get(ip_url).json()
    city = str(get_url['city'])
    return city
