import mysql.connector
from mysql.connector import Error

# Function to convert file into binary data
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Function to insert BLOB data into MySQL table
def insertBLOB(emp_id, name, photoFile, biodataFile):
    print("Inserting BLOB data into Python_Employee table")
    try:
        # connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            use_pure=True,
            database="Suresh"
        )

        cursor = connection.cursor()

        # Convert files to binary
        empPicture = convertToBinaryData(photoFile)
        biofile = convertToBinaryData(biodataFile)

        # SQL Query
        sql_insert_blob_query = """
        INSERT INTO Python_Employee (id, name, photo, biodata)
        VALUES (%s, %s, %s, %s)
        """

        # Data tuple
        insert_blob_tuple = (emp_id, name, empPicture, biofile)

        cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()

        print("Image and file inserted successfully into Python_Employee table")

    except mysql.connector.Error as error:
        print("Failed to insert BLOB data:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Insert record
insertBLOB(101, "Suresh",
           r"ManmohakShriRam.jpg",
           r"ManmohakShriRam_Image.pdf")
