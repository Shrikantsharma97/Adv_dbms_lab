import mysql.connector
conn = mysql.connector.connect(host='localhost',user = 'root',password = 'Meena@123')

mycursor = conn.cursor()
mycursor.execute("create table testDb.student_1 (name varchar(100),ROll_no INT(10), Age INT(2),marks float)");
conn.close()