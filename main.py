from db import conn, cursor

def display_employee(data):
    print("-" * 30)
    print("ID:", data[0])
    print("Name:", data[1])
    print("Age:", data[2])
    print("Gender:", data[3])
    print("Department:", data[4])
    print("Designation:", data[5])
    print("Salary:", data[6])
    print("Email:", data[7])
    print("Phone:", data[8])
    print("-" * 30)

def add_emp():
    try:
        employee_id = int(input("Enter The ID: "))
        name = input("Enter The Name: ")
        age = int(input("Enter The Age: "))
        gender = input("Enter The Gender: ")
        department = input("Enter The Department: ")
        designation = input("Enter The Designation: ")
        salary = float(input("Enter The Salary: "))
        email = input("Enthe The Email: ")
        phone = input("Enter The Phone Number: ")


        query = """INSERT INTO employees (employee_id,name,age,gender,department,designation,salary,email,phone)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(
            query,(employee_id,name,age,gender,department,designation,salary,email,phone)
        )

        conn.commit()
        print("Successfully Added Employee.....!")

    except ValueError:
        print("Please enter valid numeric values for ID, Age and Salary.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Database Error:", e)

# add_emp()

def search_emp():
    try:
            
        employee_id = int(input("Enter The ID: "))

        query = """ SELECT * FROM employees
                WHERE employee_id = %s """

        cursor.execute(query,(employee_id,))
        data = cursor.fetchone()

        if data :
            display_employee(data)
        else:
            print("Employee Not Found")    

    except ValueError:
        print("Please enter a valid Employee ID.")

    except mysql.connector.Error as e:
        print("Database Error:", e)        


# search_emp()


def view_emp():
    try:

        query = """ SELECT * FROM employees
                """

        cursor.execute(query)
        employees = cursor.fetchall()

        if employees:
            for data in employees:
                display_employee(data)

        else:
            print("Employee Not Found")    

    except mysql.connector.Error as e:
        print("Database Error:",e)    

# view_emp()


def update_emp():
    try:
        employee_id = int(input("Enter The ID: "))

        query = """ SELECT * FROM employees
                WHERE employee_id = %s """

        cursor.execute(query,(employee_id,))
        data = cursor.fetchone()

        if data :
            display_employee(data)
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
            employee_id)
                    )

        conn.commit()

        if cursor.rowcount > 0:
            print("Employee Updated Successfully")
        else:
            print("Employee Update Failed")

    except ValueError:
        print("Please enter valid numeric values for ID, Age and Salary.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Database Error:", e)
# update_emp()


def delete_emp():
    try:
        employee_id = int(input("Enter The Employee ID:"))

        query = """ 
                DELETE FROM employees
                WHERE employee_id = %s """

        cursor.execute(query,(employee_id,))
        conn.commit()

        if(cursor.rowcount>0):
            print("Employee Deleted Successfully")
        else:
            print("Employee Not Found") 

    except ValueError:
        print("Please enter a valid Employee ID.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Database Error:", e)

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

    try:
        choice = int(input("Enter The Choice: "))

        if choice == 1:
            add_emp()

        elif choice == 2:
            search_emp()

        elif choice == 3: 
            view_emp()

        elif choice == 4:
            update_emp()

        elif choice == 5:
            delete_emp()

        elif choice == 6:
            print("Thank You....")
            break
        
        else: 
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid choice.")





