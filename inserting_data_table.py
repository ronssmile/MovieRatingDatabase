from getpass import getpass
from mysql.connector import connect,Error 
from converting_csv import *

#extract data in csv 

movies_data = convert_csv(file_name="movies_records.csv")
ratings_data = convert_csv(file_name="ratings_records.csv")
reviewers_data = convert_csv(file_name="reviewers_records.csv")

try:
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter password: "),
        database = "movie_rating"
    )as connection:
        print(connection)

        #SQL Queries
        #movies table
        insert_movies_query = """
        INSERT INTO movies (title, release_year, genre, collection_in_mil)
        VALUES (%s,%s,%s,%s)
        """
        #reviewers table
        insert_reviewers_query = """
        INSERT INTO reviewers (first_name,last_name)
        VALUES (%s,%s)
        """
        #ratings table
        insert_ratings_query = """
        INSERT INTO ratings
        (rating, movie_id, reviewer_id)
        VALUES ( %s, %s, %s)
        """
        with connection.cursor() as cursor:
            """This line should be execute first since the ratings table is relational to movie_id, reviewer_id"""
            #cursor.executemany(insert_movies_query,movies_data)
            #cursor.executemany(insert_reviewers_query,reviewers_data)
            """This will be the next to be executed"""
            cursor.executemany(insert_ratings_query,ratings_data)
            connection.commit()

except Error as e:
    print(e)
