# import mysql.connector as con

# suresh = con.connect(
#     host="localhost",
#     user="root",
#     passwd="12345",
#     database="diploma"
#     use_pure=True
# )
# cr = suresh.cursor()
# cr.execute("create table employee(name varchar)")
# databases = cr.fetchall()
# print(databases)

# except Exception as e:
#     print("Error:", e)


# import mysql.connector as connection 
# mydb = connection.connect( 
#     host="localhost", 
#     user="root", 
#     passwd="12345", 
#     use_pure=True 
#     ) 
# cur=mydb.cursor() 
# cur.execute("CREATE DATABASE Suresh ")


import mysql.connector as con 
sur = con.connect( 
    host="localhost", 
    user="root", 
    passwd="12345", 
    use_pure=True 
    ) 
cur=sur.cursor() 
cur.execute("SHOW DATABASES")
databases=cur.fetchall() 
print(databases) 
