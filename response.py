import requests


def get_response(ip):
    url = "http://ip-api.com/json/"
    url_fields = '?fields=status,message,city,query'
    try:
        ip_url = url + ip + url_fields
    except TypeError:
        print('Please enter valid IP address')
        raise TypeError
    else:
        get_url = requests.get(ip_url).json()
        if get_url['status'] == 'success':
            city = get_url["city"]
            return city
        else:
            print('Sorry we`re having a problem at our end')
            return None
