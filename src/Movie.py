# Movie class, used for easier python->sql_database, and sql_database->python transformation
class Movie:
    def __init__(
        self,
        title: str = "Undefined",
        adult: bool = False,
        poster_path: str = "",
        genres: str = "Action Adventure Animation Comedy Crime Documentary Drama Family Fantasy History Horror Music Mystery Romance Science Fiction TV Movie Thriller War Western",
        release_year: int = 9999,
        vote_average: int = 0,
        vote_count: int = 0,
    ) -> None:
        self.title = title
        self.adult = adult
        self.poster_path = poster_path
        self.genres = genres
        self.release_year = release_year
        self.vote_average = vote_average
        self.vote_count = vote_count
    
    def __str__(self) -> str:
        return (
f"""Title: {self.title}
Adult: {self.adult}
Poster_path: {self.poster_path}
Genre_ids: {self.genres}
Release_year: {self.release_year}
Vote_average: {self.vote_average}
Vote_count: {self.vote_count}""")