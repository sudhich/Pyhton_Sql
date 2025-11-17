import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345"
    )

    if mydb.is_connected():
        print("Connected successfully!")
        print("Connection object:", mydb)

except Error as e:
    print("Error while connecting to MySQL:", e)
