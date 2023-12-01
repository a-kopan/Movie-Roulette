import sqlite3
from .Movie import Movie


# creates the table inside database
def create_table(db: str, table_name: str) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    # an SQL query which will check if there is a table with the same name
    checking_query = (
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    )

    # if the table already exists, just leave
    if cur.execute(checking_query).fetchone() is not None:
        return

    cur.execute(
        f"""CREATE TABLE 
                {table_name}(id PRIMARY KEY, 
                title,
                adult,
                poster_path,
                genres,
                release_year,
                vote_average,
                vote_count)"""
    )
    con.commit()
    cur.close()
    con.close()


# gets the listof movies and loads them into the database
def load_to_db(db: str, table_name: str, Movies: list) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    quer = f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    id = 1
    for movie in Movies:
        data = (
            id,
            movie.title,
            int(movie.adult),
            movie.poster_path,
            " ".join(movie.genres),
            movie.release_year,
            movie.vote_average,
            movie.vote_count,
        )

        cur.execute(quer, data)
        id += 1
        con.commit()

    cur.close()
    con.close()


# cant really tell if this is necessary
# loads specific Movies from database
"""
requirements = (min_rating: int = -1
                max_rating: int = 11
                min_production_year: int = -1
                max_production_year: int = 9999
                )
"""


def load_from_db(db: str, table_name: str, requirements: dict) -> list:
    # connection to database
    con = sqlite3.connect(db)
    cur = con.cursor()

    # query to get all the positions that meet certain requirements
    rows: list[tuple] = cur.execute(
        f"""
                       SELECT *
                       FROM {table_name}
                       WHERE
                       vote_average <= {requirements['max_rating']} AND 
                       vote_average >= {requirements['min_rating']} AND 
                       release_year >= {requirements['min_production_year']} AND 
                       release_year <= {requirements['max_production_year']}
                       """
    ).fetchall()

    # a list which will keep rows changed into Movies
    movies = list()

    # change rows into Movie objects and add them to movies
    for position in rows:
        movies.append(Movie.loaded(*position[1:]))

    return movies


# clear all records from table (but don't delete the table itself)
def clear_table(db: str, table_name: str) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute(f"DELETE FROM {table_name}")
    con.commit()

    cur.close()
    con.close()


# remove the table from database
def remove_table(db: str, table_name: str) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute(f"DROP TABLE {table_name}")
    con.commit()

    cur.close()
    con.close()
