

import mysql.connector
conn = mysql.connector.connect(host='localhost',user = 'root',
password = 'Meena@123', database = "db_1")

if conn.is_connected():
    print('Connection Successful')
mycursor=conn.cursor()