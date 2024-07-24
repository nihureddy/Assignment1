# Movie Library System

This program which is written in python manages a movie collection stored in `movies.txt`.It allows users to access all
functionalities like adding new movies, searching a movie by title or director, updating an existing  movie and deleting
movie records, User can operate these movie library system using a command-line interface.

# Features of the program:
Create: Used to add new movies with details like title, director, year and genre(optional)
Read: Used to display all movies and can search for movies by title or director.
Update: Used to modify existing movie information including title, director, year and genre.
Delete: Used to remove movies from the Movie library.

# How to Use this code:
1. Ensure Python 3.12 version is installed on your system.
2. Clone the repository and navigate to the directory.
3. Run the program using `python movie_library_system.py`.
4. Follow the menu "movie library" to perform required operations.
5. Movie data will be  saved to `movies.txt` after each operation.

# Design information :
1. Implemented classes  `Movie` and `MovieGenre` to manage movies data with and without genres.
2. Utilized dictionaries to store and retrieve movie records.
3. Included error handling for file operations and user inputs to maintain program efficiency.
