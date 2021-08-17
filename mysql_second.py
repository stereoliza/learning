from __future__ import print_function
import mysql.connector as mysql
from mysql.connector import errorcode

host = 'localhost'
user = 'root'
password = 'pass'
mydb = 'learningdb'
url = 'http://ip-api.com/json/76.170.183.186'

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
    query_values = ('76.170.183.186', str(response['regionName']['city']))
    cursor.execute(query,query_values)
    db.commit()

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
        else: 
            print(err.msg)
    else: 
        insert_data()

print(record)
cursor.close()
