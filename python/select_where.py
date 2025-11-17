

import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    use_pure=True,
    database="Suresh"
)

# Creating the cursor object
cur = myconn.cursor()

cur.execute("SELECT name, id, salary FROM Employee WHERE Dept_id=10")

# Fetching the rows from the cursor object
result = cur.fetchall()

print("Name\tid\tSalary")
for row in result:
    print("%s\t%d\t%d" % (row[0], row[1], row[2]))

myconn.close()