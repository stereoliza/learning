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
TABLES['key_value'] = (
    "CREATE TABLE IF NOT EXISTS `key_value` ("
    "  `key` varchar(25),"
    "  `value` varchar(255),"
    "  PRIMARY KEY (`key`)"
    ") ENGINE=InnoDB")


def open_db():
    try:
        table_description = TABLES['key_value']
    except mysql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            pass
    else:
        cursor.execute(table_description)


def get_from_mysql(key):
    find = "SELECT value FROM key_value WHERE key = %s"
    key_value = (key, )
    cursor.execute(find, key_value)
    record = cursor.fetchone()
    return record


def insert_data(key, response):
    insert = "INSERT INTO key_value (key, value) VALUES (%s,%s)"
    insert_values = (key, response)
    cursor.execute(insert, insert_values)
    db.commit()
