import mysql.connector
conn = mysql.connector.connect(host='localhost',user = 'root',password = 'Meena@123')

if conn.is_connected():
    print('Connection Successful')
mycursor = conn.cursor()
''''mycursor.execute("insert into sk_1.student values(1,'John Doe','john.doe@example.com','123-456-7890','123 Main St');")
mycursor.execute("insert into sk_1.student values(2,'Jane Smith','jane.smith@example.com','987-654-3210','456 Elm St');")
mycursor.execute("insert into sk_1.student values(3,'Robert Johnson','robert.j@example.com','555-123-4567','789 Oak Ave');")
mycursor.execute("insert into sk_1.student values(4,'Emily White','emily.white@example.com','111-222-3333','567 Pine St');")
mycursor.execute("insert into sk_1.student values(5,'Michael Lee','michael.lee@example.com','333-444-5555','789 Cedar Dr');")
mycursor.execute("insert into sk_1.student values(6,'Sarah Brown','sarah.brown@example.com','555-666-7777','890 Willow Ln');")
mycursor.execute("insert into sk_1.student values(7,'David Clark','david.clark@example.com','777-888-9999','123 Birch Ave');")
mycursor.execute("insert into sk_1.student values(8,'Melissa Turner','melissa.turner@example.com','888-999-0000','456 Redwood Rd');")'''

for i in range(8):
    print("Enter data for Row ",i+1)
    CourseID = int(input("Enter course ID "))
    CourseName = input("Enter Course name ")
    Credits = int(input("Enter Credits "))
    t = (CourseID,CourseName,Credits)
    print(CourseID,CourseName,Credits)
    mycursor.execute("insert into sk_1.course (CourseID,CourseName,Credits) values (CourseID,CourseName,Credits);")
    conn.commit()



conn.close()

'''for i in range(5):
    name = input("Enter Name")
    ROll_no = int(input("Enter Roll no."))
    Age = '''
    

