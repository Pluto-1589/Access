from abc import ABC, abstractmethod

# The Person class is an abstract base class that represents a generic person in the university system. It should not be instantiated directly. Methods:


class Person(ABC):

    # __init__(): Initializes the name and email attributes.
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    # get_details(): An abstract method that should be implemented by subclasses to return a tuple of the person's details.

    @abstractmethod
    def get_details(self) -> str:
        pass
