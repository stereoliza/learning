import requests
import get_ip

ipaddress = get_ip.ip
url = "http://ip-api.com/json/"

ip_url = url + ipaddress
get_response = requests.get(ip_url).json()

