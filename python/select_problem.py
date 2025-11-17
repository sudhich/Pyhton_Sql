# import mysql.connector
# from mysql.connector import Error

# try:
#     myconn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345",
#     use_pure=True,
#     database="suresh"
#     )

#     if myconn.is_connected():
#         print("Connected successfully!")
#         print("Connection object:", myconn)

# except Error as e:
#     print("Error while connecting to MySQL:", e)


# cur = myconn.cursor()

# cur.execute("SELECT * FROM employee")
# result = cur.fetchall()

# for row in result:
#     print(row)

# myconn.close()
