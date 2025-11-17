import mysql.connector

# ---------- 1. Connect to MySQL ----------
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    use_pure=True,
    database="Suresh"
)
cur = myconn.cursor()

# ---------- 2. SHOW BEFORE ----------
print("Before deleting the row")
cur.execute("SELECT name, id, salary, Dept_id, branch_name FROM Employee")
rows = cur.fetchall()

print("Name\tid\tSalary\tDept_id\tbranch_name")
for r in rows:
    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}")

# ---------- 3. DELETE THE ROW ----------
# Example: Delete the employee whose id = 104 (Raju)
cur.execute("DELETE FROM Employee WHERE id = 200")

# VERY IMPORTANT: Save the deletion!
myconn.commit()

# ---------- 4. SHOW AFTER ----------
print("\nAfter deleting the row")
cur.execute("SELECT name, id, salary, Dept_id, branch_name FROM Employee")
rows = cur.fetchall()

print("Name\tid\tSalary\tDept_id\tbranch_name")
for r in rows:
    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}")

# ---------- 5. Close ----------
cur.close()
myconn.close()