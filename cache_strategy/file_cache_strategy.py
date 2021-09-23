file = open('cache.txt', 'w+')


def get_from_file():
    response = file.read()
    print(response)
    return response


def write_in_file(response):
    file.write(response)
    print(response)


def close():
    file.close()
