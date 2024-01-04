# sends multiple API requests and returns a list with all json responses
import requests
import sys
import json


def load_API_key_from_file() -> str:
    # check if the file is in the repo, if it isn't then just quit
    try:
        f = open("API_KEY.txt")
    except:
        input(
            "No file named API_KEY.txt found.\n Try creating it in the repository and check if the name is right."
        )
        sys.exit()
    else:
        API_KEY = f.read()
        f.close()
    return API_KEY


# gets a list of 20 movies from the page specified
def send_API_request(category_code: int, page: int, API_KEY: str) -> str:
    # all filters that were left (year, length etc. will be filtered locally)
    URL = "https://advanced-movie-search.p.rapidapi.com/discover/movie"
    # get 3 pages (3 separate requests, because this API returns only 20 movies at once)
    querystring = {"with_genres": str(category_code), "page": str(page)}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "advanced-movie-search.p.rapidapi.com",
    }

    response = requests.get(URL, headers=headers, params=querystring)
    return response.json()


def send_n_API_requests_with_key(
    category_code: int, n_of_pages: int, API_KEY: str
) -> list:
    # set that holds all json responses
    json_responses = []
    for page_num in range(0, n_of_pages):
        response = send_API_request(category_code, page_num + 1, API_KEY)
        json_responses.append(response)
    return json_responses


def send_n_API_requests(category_code: int, n_of_pages: int) -> json:
    API_KEY = load_API_key_from_file()

    # set that holds all json responses
    json_responses = []
    for page_num in range(0, n_of_pages):
        response = send_API_request(category_code, page_num + 1, API_KEY)
        json_responses.append(response)
    return json_responses
