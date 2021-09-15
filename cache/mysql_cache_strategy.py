import mysql.connector as mysql
from mysql.connector import errorcode
from get_url import get_response
from get_ip import ip


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
        mysql_response = get_response
        query = 'INSERT INTO location(ip,address) VALUES (%s,%s)'
        query_values = (ip, str(mysql_response['city']))
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