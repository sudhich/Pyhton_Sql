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

# Create a table
cur.execute("""
CREATE TABLE Employee2(
    name VARCHAR(20) NOT NULL,
    id INT PRIMARY KEY,
    salary FLOAT NOT NULL,
    Dept_id INT NOT NULL
)
""")

myconn.close()
