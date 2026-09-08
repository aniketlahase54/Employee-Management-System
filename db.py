import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database = "employee_db",
    user="root",
    password="password",
    port = 3306
    
)

cursor = conn.cursor()