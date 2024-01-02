# filters requests from json format to Movie class
from src.Movie import Movie
import json


# Transforms a singular json object into a movie object
def json_to_Movie(json_object: json) -> Movie:
    movie = Movie(
        title=json_object["title"],
        adult=json_object["adult"],
        poster_path=json_object["poster_path"],
        genres=' '.join([name for (name, id) in genre_list.items() if id in json_object["genre_ids"]]),
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

genre_list = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37,
}
