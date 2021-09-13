from __future__ import print_function
import mysql.connector as mysql
from mysql.connector import errorcode
import requests
import redis, json

url = 'http://ip-api.com/json/76.170.183.186'
ip = '76.170.183.186'


def cache_in_file():
    response = None
    try:
        response = open('response.txt', 'w+')
        location = response.read()
        if location !='':
            location = response.read()
            print(location)
        else:
            response = open('response.txt', 'w')
            location = requests.get(url).json()
            response.write(str(location['city']))
            print(str(location['city']))
    finally:
        if response:
            response.close()


def cache_in_mysql():
    host = 'localhost'
    user = 'root'
    password = 'pass'
    mydb = 'learningdb'


    db = mysql.connect(host=host,
                       user=user,
                       password=password,
                       database=mydb)
    cursor = db.cursor()

    TABLES = {}
    TABLES['location'] = (
        "CREATE TABLE `location` ("
        "  `ip` varchar(25),"
        "  `address` varchar(255),"
        "  PRIMARY KEY (`ip`)"
        ") ENGINE=InnoDB")


    def insert_data():
        response = requests.get(url).json()
        query = 'INSERT INTO location(ip,address) VALUES (%s,%s)'
        query_values = (ip, str(response['city']))
        cursor.execute(query, query_values)


    for location in TABLES:
        table_description = TABLES['location']
        try:
            cursor.execute(table_description)
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                cursor.execute('SELECT address from location')
                record = cursor.fetchone()
                if record is None:
                    insert_data()
                    cursor.execute('SELECT address from location')
                    record = cursor.fetchone()
            else:
                print(err.msg)
        else:
            insert_data()


    print(record)
    cursor.close()


def cache_in_redis():
    redis_client = redis.Redis(host ='localhost', port=6379, db=0)

    response = redis_client.get('location')
    if response is None:
        response = requests.get(url).json()
        redis_client.set('location', str(response['city']))
    else:
        response = json.loads(response)

    response = redis_client.get('location')
    print(response)
