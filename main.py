import src.API.json_to_Movie as jtM
import src.db_calls as dbc


def main():
    test_json = open(r"tests\test_json.json", encoding="utf-8")
    movies = jtM.responses_to_movies(test_json.read())
    # [print(movie.title, end="\n") for movie in movies]
    db_path = r"database\Movie_db.db"
    table_name = "Movies_table"
    dbc.clear_table(db_path, table_name)
    dbc.create_table(db_path, table_name)
    dbc.load_to_db(db_path, table_name, movies)

    temp_requirements = dict()
    temp_requirements["min_rating"] = -1
    temp_requirements["max_rating"] = 11
    temp_requirements["min_production_year"] = -1
    temp_requirements["max_production_year"] = 9999

    movies_from_db = dbc.load_from_db(db_path, table_name, temp_requirements)
    a = 0


if __name__ == "__main__":
    main()
