# filters requests from json format to Movie class
from ..Movie import Movie
import json


# transforms a singular json object into a movie object
def json_to_Movie(json_object: json) -> Movie:
    movie = Movie(
        title=json_object["title"],
        adult=json_object["adult"],
        poster_path=json_object["poster_path"],
        genre_ids=json_object["genre_ids"],
        release_year=int(json_object["release_date"].split("-")[0]),
        vote_average=json_object["vote_average"],
        vote_count=json_object["vote_count"],
    )
    return movie


# transform a list of json objects into movie list
def response_to_movies(response_list: list) -> list:
    movies = []
    for object in response_list["results"]:
        movies.append(json_to_Movie(object))
    return movies


# transform a list of lists of json objects into a singular movie list
def responses_to_movies(list_of_responses: json) -> list:
    list_of_responses = json.loads(list_of_responses)
    movies = []
    for response_list in list_of_responses:
        movies.extend(response_to_movies(response_list))
    return movies
