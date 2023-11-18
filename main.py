import src.API.filter_requests as fr
import json
def main():
    test_json = open(r'tests\test_json.json',encoding='utf-8')
    movies = fr.responses_to_movies(test_json.read())
    [print(movie.title, end="\n") for movie in movies]
    
if __name__ == "__main__":
    main()