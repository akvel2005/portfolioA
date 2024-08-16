import mysql.connector


def create_and_view_customers():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your username
        password="412005",  # Replace with your password
        database="shan"  # Replace with your database name
    )
    if mydb:
        print("connection sucees")
    else:
        print("connection error")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM new_table")
    rows = mycursor.fetchall()

    for i in rows:
        for j in i:
            print(j, end = ' ')
        print()

    # Close the cursor and the database connection
    mycursor.close()
    mydb.close()

create_and_view_customers()