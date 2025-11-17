import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    use_pure=True,
    database="suresh"
)

# creating cursor
cur = myconn.cursor()

# reading data
cur.execute("SELECT * FROM employee")

# retrieving all rows
result = cur.fetchall()

# printing rows
for item in result:
    print(item)

myconn.close()

