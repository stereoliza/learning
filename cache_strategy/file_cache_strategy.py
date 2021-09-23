file = open('address.txt', 'w+')


def get_from_file():
    location = file.read()
    print(location)
    return location


def write_in_file(response):
    file.write(response)
    print(response)


def close():
    file.close()
