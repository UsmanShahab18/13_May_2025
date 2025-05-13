import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # XAMPP default MySQL password is empty
    database="student_managment_with_python"  # Replace with your database name
)

cursor = conn.cursor()

# # Run a test query
# cursor.execute("SHOW TABLES")
#
# # Print the results
# for table in cursor:
#     print(table)

# Run SELECT query
cursor.execute("SELECT * FROM student_info")

# Fetch and print each name (column index 0)
results = cursor.fetchall()
for row in results:
    # print(row)
    print("Student Id:", row[0])
    print("Student Name:", row[1])
    print("Student Address:", row[2])
    print("Student Phone:", row[3])

# Close connection
cursor.close()
conn.close()
