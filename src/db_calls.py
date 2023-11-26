import sqlite3


# creates the table inside database
def create_table(db: str, table_name: str) -> None:
    con = sqlite3.connect(db)

    cur = con.cursor()

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


# loads specific Movies from database
"""
requirements = (min_rating: int = -1
                max_rating: int = 101
                min_production_year: int = -1
                max_production_year: int = 9999
                )
"""


def from_db(db: str, requirements: dict) -> None:
    pass
