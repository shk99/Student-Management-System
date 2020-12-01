import mysql.connector

def student():
    print('''Welcome Student
        1. Register
        2. View Courses
        3. Apply for a Course''')
    choice = input('\nYou want to ????? :')

    if choice == '1':
        name = input("Enter Student name :")
        dob = input("Students' date of birth :")
        mycursor.execute("INSERT INTO student (NAME,DOB) VALUES (%s, %s)", (name, dob))
        mydb.commit()   

    if choice == '2':
        print('Here is a list of all courses :')     
        mycursor.execute("select * from course")
        for x in mycursor:
            print(x)

    if choice == '3':
        name = input('Please enter your name :')
        print('Now please choose 1 course from the following available courses :')
        print('')
        mycursor.execute("select * from course")
        for x in mycursor:
            print(x)
        c_id = input('Now please enter course id you wish to enroll in :')
        mycursor.execute("update student set COURSEID = %s where NAME = %s", (c_id, name))
        mydb.commit()

def admin():
    print('''Welcome Admin
        1. Add a new Course
        2. View Courses
        3. View Student''')
    choice = input('\nYou want to ?????:')

    if choice == '1':
        course = input("\nEnter course name:")
        course_id = input('\nEnter course ID:')
        duration = input('Enter course duration(in years):')
        fees = input("Enter fees for course:")
        mycursor.execute("INSERT INTO course VALUES (%s, %s, %s, %s)", (course_id, course, duration, fees))
        mydb.commit()
    
    if choice == '2':
        print("\nHere a list of all the available courses")
        mycursor.execute("select * from course")
        for x in mycursor:
            print(x)

    if choice == '3':
        roll_no = input('Enter your roll no : ')
        sql_select_query = """select * from student where ROLLNO = %s"""
        mycursor.execute(sql_select_query, (roll_no,))
        record = mycursor.fetchall()
        print(record)
        
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shoaib"
)

mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)

print("Welcome to Student Management System")
choice = input('''
Tell us who you are:
1. Student
2. Admin\n''')

if choice == '1': student()
if choice == '2' : admin()