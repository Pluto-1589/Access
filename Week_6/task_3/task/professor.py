
from person import Person

# The Professor class represents a professor teaching at the university.


class Professor(Person):

    # __init__(): Initializes the professor with name, email, employee_id, and office.
    def __init__(self, name: str, email: str, employee_id: str, office: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.office = office

        # get_details(): Returns a tuple containing the professor's details (name, email, employee_id, office).
    def get_details(self) -> str:
        return (self.name, self.email, self.employee_id, self.office)
