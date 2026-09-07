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

def search_emp():
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
        


# search_emp()


def view_emp():

    query = """ SELECT * FROM employees
             """

    cursor.execute(query)
    employees = cursor.fetchall()

    if employees:
        for data in employees:
            print("ID: ",data[0])
            print("Name:",data[1])
            print("Age:",data[2])
            print("Gender:",data[3])
            print("Department:",data[4])
            print("Designation:",data[5])
            print("Salary:",data[6])
            print("Email:",data[7])
            print("Phone:",data[8])
            print("-" * 30)

    else:
        print("Employee Not Found")    
        

# view_emp()


def update_emp():
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
        return


    Update_Name = input("Enter The Update Name: ") or data[1]
    age_input = input("Enter The Update Age: ")
    Update_Age = int(age_input) if age_input else data[2]
    Update_Gender = input("Enter The Update Gender: ") or data[3]
    Update_Department = input("Enter The Update Department: ") or data[4] 
    Update_Designation = input("Enter The Update Designation: ") or data[5]
    salary_input = input("Enter The Update Salary: ")
    Update_Salary = float(salary_input) if salary_input else data[6]
    Update_Email = input("Enthe The Update Email: ") or data[7]
    Update_Phone = input("Enter The Update Phone Number: ") or data[8]



    update_query = """
                    UPDATE employees
                    SET name = %s ,
                    age = %s ,
                    gender = %s ,
                    department = %s ,
                    designation = %s,
                    salary = %s ,
                    email = %s,
                    phone = %s
                    WHERE employee_id = %s 
                    """     

    cursor.execute(
        update_query,(Update_Name,
        Update_Age,
        Update_Gender,
        Update_Department,
        Update_Designation,
        Update_Salary,
        Update_Email,
        Update_Phone,
        ID)
                )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee Updated Successfully")
    else:
        print("Employee Update Failed")

# update_emp()


def delete_emp():
    ID = int(input("Enter The Employee ID:"))

    query = """ 
            DELETE FROM employees
            WHERE employee_id = %s """

    cursor.execute(query,(ID,))
    conn.commit()

    if(cursor.rowcount>0):
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found") 

# delete_emp()        

while True:
    print("=========================EMPLOYEE MANAGEMENT SYSTEM======================")

    print("1. Add Employee")
    print("2. Search Employee")
    print("3. View All Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("===============================================")
    
    choice = int(input("Enter The Choice: "))

    if choice == 1:
        add_emp()

    elif choice == 2:
        search_emp()

    elif choice == 3: 
        view_emp()

    elif choice == 4:
        update_emp()

    elif choise == 5:
        delete_emp()

    elif choise == 6:
        print("Thank You....")
        break
    
    else: 
        print("Invalid Choice")





