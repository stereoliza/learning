import mysql.connector as mysql
from mysql.connector import errorcode

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
TABLES['city_ip'] = (
    "CREATE TABLE IF NOT EXISTS `city_ip` ("
    "  `ipaddress` varchar(25),"
    "  `address` varchar(255),"
    "  PRIMARY KEY (`ipaddress`)"
    ") ENGINE=InnoDB")


def open_db():
    try:
        table_description = TABLES['city_ip']
    except mysql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            pass
    else:
        cursor.execute(table_description)


def get_from_mysql(ip):
    find = "SELECT address FROM city_ip WHERE ipaddress = %s"
    ip_value = (ip, )
    cursor.execute(find, ip_value)
    record = cursor.fetchone()
    return record


def insert_data(ip, response):
    insert = "INSERT INTO city_ip (ipaddress, address) VALUES (%s,%s)"
    insert_values = (ip, response)
    cursor.execute(insert, insert_values)
    db.commit()
