import src.API.json_to_Movie as jtM
import src.db_calls as dbc


def main():
    test_json = open(r"tests\test_json.json", encoding="utf-8")
    movies = jtM.responses_to_movies(test_json.read())
    # [print(movie.title, end="\n") for movie in movies]
    db_path = r"database\Movie_db.db"
    table_name = "Movie_db"
    # dbc.create_table(db_path,table_name)
    dbc.load_to_db(db_path, table_name, movies)


if __name__ == "__main__":
    main()
