#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie


class MovieBox:
    def __init__(self, title: str, movies: list):

        if any(not isinstance(movie, Movie) for movie in movies):
            raise Warning("All entries in movies must be instances of Movie")
        if not title:
            raise Warning("Empty title is provided")
        if not movies:
            raise Warning("Empty movies list provided")

        self.title = title
        self.movies = movies

    def __repr__(self) -> str:
        movies_repr = ", ".join(repr(movie) for movie in self.movies)
        return f"MovieBox(\"{self.title}\", [{movies_repr}])"

    def __eq__(self, other: object) -> bool:

        return isinstance(other, MovieBox) and self.title == other.title and self.movies == other.movies

    def __hash__(self) -> int:
        return hash((self.title, tuple(self.movies)))

    def get_title(self):

        return self.title

    def get_actors(self):

        actors = set()

        for movie in self.movies:
            actors.update(movie.get_actors())

    def get_duration(self):
        return sum(movie.get_duration() for movie in self.movies)
