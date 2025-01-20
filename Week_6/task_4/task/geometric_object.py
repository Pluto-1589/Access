from abc import ABC, abstractmethod


class GeometricObject(ABC):

    def __init__(self, color: str, filled: bool):
        self.color = color
        self.filled = filled

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass
