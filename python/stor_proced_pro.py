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
cur.execute("DROP TABLE IF EXISTS Employee")
cur.execute("""
CREATE TABLE Employee(
    name VARCHAR(20) NOT NULL,
    id INT PRIMARY KEY,
    salary FLOAT NOT NULL,
    Dept_id INT NOT NULL
)
""")
print("Table created successfully!")

# Insert sample data
cur.execute("INSERT INTO Employee VALUES('Ravi', 1, 50000, 10)")
cur.execute("INSERT INTO Employee VALUES('Priya', 2, 60000, 20)")
cur.execute("INSERT INTO Employee VALUES('Amit', 3, 55000, 10)")
myconn.commit()
print("Sample data inserted!")

# Create stored procedure
cur.execute("DROP PROCEDURE IF EXISTS GetEmployeeById")
cur.execute("""
CREATE PROCEDURE GetEmployeeById(IN emp_id INT)
BEGIN
    SELECT * FROM Employee WHERE id = emp_id;
END
""")
print("Stored Procedure created!")

# Call stored procedure
args = [2]
cur.callproc('GetEmployeeById', args)

# Display results
print("\nEmployee Details:")
# Fetch results directly without stored_results()
cur.execute("SELECT * FROM Employee WHERE id = %s", (2,))
row = cur.fetchone()
if row:
    print(f"Name: {row[0]}, ID: {row[1]}, Salary: {row[2]}, Dept: {row[3]}")

cur.close()
myconn.close()
