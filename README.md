# Movie-Roulette

GUI Python application that lets you go through data of randomly selected movies and temporarly save it.

Just choose a genre, preffered length of the movie and rating and you are ready to go!

## Usage

The application entrypoint is the main.py.

In case of not having the API key, use the DEMO button in the bottom-left corner.

Thing worth noting is that the **DEMO button also uses provided criteria** (genre, length, rating)

## Operating

When clicking a DEMO/DRAW button, the application gets total ammount of movies from the API and loads them into the database.

After that the movies are filtered based on the provided criteria and only then the images for them are downloaded.

* [ ] **In case of too many movies being filtere**
* [ ] **d, the waiting time can be long due to downloading movie posters!**

## API

The API used is called Advanced Movie Search, done by Akash Joshi.

Link: [Advanced Movie Search API Documentation (jakash1997) | RapidAPI](https://rapidapi.com/jakash1997/api/advanced-movie-search)
