import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database = "employee_db",
    user="root",
    password="password",
    port = "3306"
    
)

cursor = conn.cursor()

def add_emp():
    ID = int(input("Enter The ID: "))
    Name = input("Enter The Name: ")
    Age = int(input("Enter The Age: "))
    Gender = input("Enter The Gender: ")
    Department = input("Enter The Department: ")
    Designation = input("Enter The Designation: ")
    Salary = float(input("Enter The Salary: "))
    Email = input("Enthe The Email: ")
    Phone = input("Enter The Phone Number: ")


    query = """INSERT INTO employees (employee_id,name,age,gender,department,designation,salary,email,phone)
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    cursor.execute(
        query,(ID,Name,Age,Gender,Department,Designation,Salary,Email,Phone)
    )

    conn.commit()
    print("Successfully Added Employee.....!")

# add_emp()

def view_emp():
    ID = int(input("Enter The ID: "))

    query = """ SELECT * FROM employees
            WHERE employee_id = %s """

    cursor.execute(query,(ID,))
    data = cursor.fetchone()

    if data :
        print("ID: ",data[0])
        print("Name:",data[1])
        print("Age:",data[2])
        print("Gender:",data[3])
        print("Department:",data[4])
        print("Designation:",data[5])
        print("Salary:",data[6])
        print("Email:",data[7])
        print("Phone:",data[8])

    else:
        print("Employee Not Found")    
        


view_emp()


def view_emp():

    query = """ SELECT * FROM employees
             """

    cursor.execute(query,)
    data = cursor.fetchone()

    if data :
        print("ID: ",data[0])
        print("Name:",data[1])
        print("Age:",data[2])
        print("Gender:",data[3])
        print("Department:",data[4])
        print("Designation:",data[5])
        print("Salary:",data[6])
        print("Email:",data[7])
        print("Phone:",data[8])

    else:
        print("Employee Not Found")    
        

# view_emp()