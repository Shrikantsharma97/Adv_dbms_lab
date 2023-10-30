import mysql.connector
conn = mysql.connector.connect(host='localhost',user = 'root',password = 'Meena@123')

mycursor = conn.cursor()
mycursor.execute("insert testDb.student_1 values('Shrikant', 21, 21, 82.5);")
mycursor.execute("insert testDb.student_1 values('DJ', 22, 21, 81.5);")
mycursor.execute("insert testDb.student_1 values('Bose', 22, 21, 81.5);")
mycursor.execute("insert testDb.student_1 values('BADA', 22, 21, 99);")
conn.commit()
conn.close()

'''for i in range(5):
    name = input("Enter Name")
    ROll_no = int(input("Enter Roll no."))
    Age = '''
    

