from getpass import getpass
from mysql.connector import connect,Error

try:
    #connect to your local existing database(mysql)
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter password: "),
        database = "movie_rating",
    )as connection:
        print(connection)
        
    #quries to create a table
        create_movies_table_query = """
    CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil DECIMAL (4,1)
    )
    """
        create_reviewers_table_query="""
    CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
    )           
    """
        create_ratings_table_query = """
    CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
    )
    """     
        #this will create a table
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            connection.commit()

except Error as e:
    print(e)
