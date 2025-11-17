import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    use_pure=True,
    database="suresh"
)
# creating the cursor object
cur = myconn.cursor()

# Add new column to the table
cur.execute("ALTER TABLE Employee ADD branch_name VARCHAR(20) NOT NULL")

myconn.close()
