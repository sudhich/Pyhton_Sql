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


cur.execute('INSERT INTO employee(name, id, salary, Dept_id) VALUES ("Sudhir", 200, 9700, 70)')
myconn.commit()

print(cur.rowcount, "record(s) inserted!")
myconn.close()
