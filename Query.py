import mysql.connector
conn = mysql.connector.connect(host='localhost',user = 'root',password = 'Meena@123')

mycursor = conn.cursor()
mycursor.execute("select * from testDb.student_1;")
for i in mycursor.fetchall():
    print(i)

conn.close()