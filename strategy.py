import functions2

url = 'http://ip-api.com/json/76.170.183.186'
ip = '76.170.183.186'


def find_location(param='in_file'):
    if param == 'in_file':
        functions2.cache_in_file()
    elif param == 'in_mysql':
        functions2.cache_in_mysql()
    elif param == 'in_redis':
        functions2.cache_in_redis()
    else:
        print('Can not find location, try again')


find_location('in_file')
find_location('in_mysql')
find_location('in_redis')