"""
Python Assignment: Movie Library System
Background:
You need to develop a program to manage movie collection. The program should handle adding new movies, searching for
movies by title or director, and categorizing movie by genre.

The data will be stored in a file (movies.txt) and managed using classes, dictionaries, and file handling techniques.

Save new movie records or updated records back to the file.

Requirements:

Class Definitions:
Create a base class Movie with the following attributes:
title: Title of the Movie (string)
director: Director of the movie (string)
year: Year of release (integer)
Subclass for movie genre:
Define a subclass MovieGenre inheriting from Movie with an additional attribute:
genre: Genre of the movie (string)
Implement the following operations:
Create: Add a new movie record
Read: Display all movies or search for a specific movie by title or director
Update: Modify an existing movie information (title, director, year, genre)
Delete: Remove a movie record

Menu System:
Create a simple command-line interface with a menu that allows users to select and perform above operations.
Handle user input validation to ensure data integrity.

Advanced Concepts:
Use dictionaries to store and manage movie records efficiently.
Implement error handling for file operations and user inputs.
Include docstrings and comments to explain the functionality of classes and functions.

Testing and Documentation:
Test your program with various scenarios (e.g., adding new movie, updating records, handling errors).
Document your code with comments and a brief README explaining how to run the program and any design decisions made.
has context menu
"""


class Movie:
    """ Class Movie is a base class to represent attributes title,director and year """
    def __init__(self, title, director, year):
        """ Initializes a Movie object with title, director, and year."""
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        """ Returns a string representation of the Movie object """
        return f"{self.title},directed by {self.director},released in the year {self.year}"


class MovieGenre(Movie):
    """ Subclass MovieGenre inheriting from class Movie, adding a genre attribute """
    def __init__(self, title, director, year, genre):
        Movie.__init__(self, title, director, year)

        '''super().__init__(title,director,year)'''
        '''can also use super function to inherit'''
        self.genre = genre

    def __str__(self):
        return f"{self.title},directed by {self.director},released in the year {self.year},genre is {self.genre}"


def load_movies(file):
    """ Loads movies data from a file and returns a dictionary of Movie objects """
    movies = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) < 3 or len(data) > 4:
                    print("invalid data format")
                    continue
                title = data[0]
                director = data[1]
                year = int(data[2])
                if not (1800 <= year <= 2100):
                    print("Year must be between 1800 and 2100")
                    return
                if len(data) == 4:
                    genre = data[3]
                    movies[title] = MovieGenre(title, director, int(year), genre)
                else:
                    movies[title] = Movie(title, director, int(year))
    except FileNotFoundError:
        print(f"{file} not found")
    return movies


def save_movies(file, movies):
    """ Saves movies data to a file """
    try:
        with open(file, 'w') as f:
            for movie in movies.values():
                if isinstance(movie, MovieGenre):
                    f.write(f"{movie.title},{movie.director},{movie.year},{movie.genre}\n")
                else:
                    f.write(f"{movie.title},{movie.director},{movie.year}\n")
        print(f"saved movies to '{file} ")
    except IOError:
        print("failed saving data to the file")


def add_movie(file, title, director, year, genre=None):
    """ Adds a new movie data to the movie library """
    movies = load_movies(file)
    if title.strip() == "" or director.strip() == "":
        print("this field cant be empty")
    if title in movies:
        print(f"Movie '{title}' already exists.")
        return
    if genre:
        movies[title] = MovieGenre(title, director, year, genre)
    else:
        movies[title] = Movie(title, director, year)
    save_movies(file, movies)
    print(f"Added movie: {movies[title]}")


def display_movies(file):
    """ Displays all the current movies in the movie library """
    movies = load_movies(file)
    if not movies:
        print("No movies found.")
    else:
        for movie in movies.values():
            print(movie)


def search_movie(file, search_type, query):
    """ Search for the movies in the movie library by title or director """
    movies = load_movies(file)
    found = False
    for movie in movies.values():
        if search_type == 'title' and query.lower() in movie.title.lower():
            print(movie)
            found = True

        elif search_type == 'director' and query.lower() in movie.director.lower():
            print(movie)
            found = True
    if not found:
        print(f"No movies found with {search_type} '{query}'.")


def update_movie(file, title, director, year, genre=None):
    """ Updates an existing movie's information in the movie library """
    movies = load_movies(file)
    if title in movies:
        movie = movies[title]
        movie.director = director
        movie.year = year
        if genre:
            movie.genre = genre
        else:
            movie.genre = None

        save_movies(file, movies)
        print(f"Updated movie: {movie}")
    else:
        print(f"Movie with title '{title}' not found.")


def delete_movie(file, title):
    """ Deletes a movie from the movie library """
    movies = load_movies(file)
    if title in movies:
        del movies[title]
        save_movies(file, movies)
        print(f"Deleted movie with title '{title}'.")
    else:
        print(f"Movie with title '{title}' not found.")


def movie_library(file):
    """ Command-line interface for interacting with the movie library system """
    while True:
        print("   Movie Library Menu   ")
        print("1. to add a new movie")
        print("2. to display all movies")
        print("3. to search for a movie by title")
        print("4. to search for a movie by director")
        print("5. to update movie info")
        print("6. to delete movie")
        print("7. exit")

        option = input("Enter your option from 1 to 7: ")

        if option == '1':
            title = input("Enter title: ")
            director = input("Enter director: ")
            year = int(input("Enter year of release: "))
            genre = input("Enter genre (leave blank if none): ").strip()
            add_movie(file, title, director, year, genre)

        elif option == '2':
            display_movies(file)

        elif option == '3':
            title = input("Enter title to search: ")
            search_movie(file, 'title', title)

        elif option == '4':
            director = input("Enter director to search: ")
            search_movie(file, 'director', director)

        elif option == '5':
            title = input("Enter title of the movie to update: ")
            director = input("Enter new director name: ")
            year = int(input("Enter new year of release: "))
            genre = input("Enter new genre (leave blank if none): ").strip()
            update_movie(file, title, director, year, genre)

        elif option == '6':
            title = input("Enter title of the movie to delete: ")
            delete_movie(file, title)

        elif option == '7':
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please, enter a number from 1 to 7.")


file = "movies.txt"
movie_library(file)
