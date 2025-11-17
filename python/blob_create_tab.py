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
CREATE TABLE Python_Employee(
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    photo BLOB NOT NULL,
    biodata BLOB NOT NULL,
    PRIMARY KEY(id)        
)
""")

myconn.close()
