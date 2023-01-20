from getpass import getpass
from mysql.connector import connect,Error

try:
    #connect to your local database workbench(mysql)
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter password: ")
    )as connection:
        print(connection)

        #SQL Query
        create_db_query = "CREATE DATABASE movie_rating"

        #it will process and make a database
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            connection.commit()

except Error as e:
    print(e)