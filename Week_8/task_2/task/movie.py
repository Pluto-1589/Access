# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    # Raise a Warning when an empty title or an empty list of actors is provided or when the duration is not at least one minute.
    def __init__(self, title: str, actors: list, duration: float):

        if not actors:
            raise Warning("Empty list of actors is provided")
        if not title:
            raise Warning("Empty title is provided")
        if duration < 1:
            raise Warning("Duration is less than one minute")

        self. title = title
        self.__actors = actors
        self.duration = duration

    def get_title(self):
        return self.title

    def get_actors(self):
        return self.__actors

    def get_duration(self):
        return self.duration

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Movie) and self.duration == other.duration and self.__actors == other.__actors and self.title == other.title

    def __hash__(self) -> int:
        return hash((self.title, tuple(self.__actors), self.duration))

    def __repr__(self) -> str:

        def format_quotes(actors):
            return '[' + ', '.join(f'"{actor}"' for actor in actors) + ']'

        return f"Movie(\"{self.title}\", {format_quotes(self.__actors)}, {self.duration})"
