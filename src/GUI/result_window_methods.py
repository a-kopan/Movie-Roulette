from src.Movie import Movie

# Add the first and last movie templates into the queue
def add_templates(movies:list[Movie]):
    first_template = Movie("First")
    last_template = Movie("Second")
    
    movies.insert(0,first_template)
    movies.append(last_template)