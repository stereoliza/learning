import mysql.connector as mysql
import json
import requests

host = 'localhost'
user = 'root'
password = 'pass'

db = mysql.connect(host=host,user=user,password=password,database='learningdb')
cursor = db.cursor()

cursor.execute('SELECT address from location')
record = cursor.fetchone()

if record is None:
    response = requests.get("http://ip-api.com/json/76.170.183.186").json()
    query = 'INSERT INTO location(ip,address) VALUES (%s,%s)'
    query_values = ('76.170.183.186', str(response['city']))
    cursor.execute(query,query_values)
    db.commit()

print(record)