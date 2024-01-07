# Tests if the Movie class creates the objects correctly
import unittest
import json
from ..API.json_to_Movie import *

# Test file on which everything will be checked
test_file = open(r"test_json.json", encoding="utf-8")
test_file = json.loads(test_file.read())


class MovieTest(unittest.TestCase):
    # First movie on the list
    movie_s = test_file[0]["results"][0]
    movie_obj = json_to_Movie(movie_s)

    # Test loading singular json object
    def test_title(self):
        self.assertEqual(self.movie_obj.title, "Five Nights at Freddy's")

    # Test loading singular json object
    def test_adult(self):
        self.assertEqual(self.movie_obj.adult, False)

    # Test loading singular json object
    def test_poster_path(self):
        self.assertEqual(
            self.movie_obj.poster_path,
            "https://image.tmdb.org/t/p/original/A4j8S6moJS2zNtRR8oWF08gRnL5.jpg",
        )

    # Test loading singular json object
    def test_poster_genres(self):
        self.assertEqual(self.movie_obj.genres, "Horror Mystery")

    # Test loading singular json object
    def test_release_date(self):
        self.assertEqual(self.movie_obj.release_year, 2023)

    # Test loading singular json object
    def test_vote_average(self):
        self.assertEqual(self.movie_obj.vote_average, 8)

    # Test loading singular json object
    def test_vote_count(self):
        self.assertEqual(self.movie_obj.vote_count, 2144)
