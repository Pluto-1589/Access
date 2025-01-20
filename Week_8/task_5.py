import re


class Publication:

    def __init__(self, authors: list, title: str, year: int):
        self.__authors = tuple(authors)
        self.__title = title
        self.__year = year

    def __repr__(self) -> str:

        def format_quotes(authors):
            return '[' + ', '.join(f'"{author}"' for author in authors) + ']'

        return f"Publication({format_quotes(list(self.__authors))}, \"{self.__title}\", {self.__year})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Publication):
            return NotImplemented

        return self.__authors == other.__authors and self.__title == other.__title and self.__year == other.__year

    def __hash__(self) -> int:
        return hash((self.__authors, self.__title, self.__year))

    def get_authors(self):
        return list(self.__authors)

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __le__(self, other):

        if not isinstance(other, Publication):
            return NotImplemented

        return (self.__authors, self.__title, self.__year) <= (other.__authors, other.__title, other.__year)

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) < (other.__authors, other.__title, other.__year)

    def __ne__(self, other):

        return not self == other

    def __gt__(self, other):

        if not isinstance(other, Publication):
            return NotImplemented

        return (self.__authors, self.__title, self.__year) > (other.__authors, other.__title, other.__year)

    def __ge__(self, other):

        if not isinstance(other, Publication):
            return NotImplemented

        return (self.__authors, self.__title, self.__year) >= (other.__authors, other.__title, other.__year)


if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"],
                    "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"],
                    "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"],
                    "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {p1: 273, p2: 398, }
