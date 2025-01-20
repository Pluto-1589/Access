# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library:

    def __init__(self):
        self.movies = set()

    def add_movie(self, movie):

        if not isinstance(movie, (Movie, MovieBox)):
            raise Warning("Only Movie or MovieBox instances can be added")

        self.movies.add(movie)

    def get_movies(self):

        def extract_movies(item):
            if isinstance(item, MovieBox):
                all_movies = []

                for movie in item.movies:
                    all_movies.extend(extract_movies(movie))
                return all_movies

            elif isinstance(item, Movie):
                return [item]

            return []

        unique_movies = {
            movie for item in self.movies for movie in extract_movies(item)}

        return sorted(unique_movies, key=lambda x: x.get_title())

    def get_total_duration(self):

        return sum(movie.get_duration() for movie in self.get_movies())
