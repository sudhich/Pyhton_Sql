
import mysql.connector as connection

mydb = connection.connect(
    host="localhost", 
    user="root", 
    passwd="12345", 
    database="testDB", 
    use_pure=True
)

# check if the connection is established
print(mydb.is_connected())
