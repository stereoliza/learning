from get_url import get_response


def cache_in_file():
    file_response = None
    try:
        file_response = open('address.txt', 'w+')
        location = file_response.read()
        if location !='':
            location = file_response.read()
            print(location)
        else:
            file_response = open('address.txt', 'w')
            location = get_response
            file_response.write(str(location['city']))
            print(str(location['city']))
    finally:
        if file_response:
            file_response.close()