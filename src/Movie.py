# Movie class, used for easier python -> sql_database transformation
class Movie:
    def __init__(
        self,
        title: str = "Undefined",
        adult: bool = True,
        poster_path: str = "",
        genre_ids: list = [],
        release_year: int = 9999,
        vote_average: int = 0,
        vote_count: int = 0,
    ) -> None:
        self.title = title
        self.adult = adult
        self.poster_path = poster_path
        self.genres = {name: id for (name, id) in genres.items() if id in genre_ids}
        self.release_year = release_year
        self.vote_average = vote_average
        self.vote_count = vote_count

    # A constructor but suited for scenario of loading Movie from the database,
    # instead of genre_ids you get genres, which are a string representation of genre ids
    @classmethod
    def loaded(
        self,
        title: str = "Undefined",
        adult: int = 1,
        poster_path: str = "",
        genres: list = [],
        release_year: int = 9999,
        vote_average: int = 0,
        vote_count: int = 0,
    ):
        self.title = title
        self.adult = adult == 1
        self.poster_path = poster_path
        self.genres = genres
        self.release_year = release_year
        self.vote_average = vote_average
        self.vote_count = vote_count
        return self

    def __str__(self) -> str:
        return f"""Title: {self.title}
Adult: {self.adult}
Poster_path: {self.poster_path}
Genre_ids: {self.genres}
Release_year: {self.release_year}
Vote_average: {self.vote_average}
Vote_count: {self.vote_count}"""


genres = {
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
