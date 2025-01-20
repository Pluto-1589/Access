from person import Person

# The Student class represents a student enrolled at the university.


class Student(Person):

    # __init__(): Initializes the student with name, email, and student_id.
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id

    # get_details(): Returns a tuple containing the student's details (name, email, student_id).

    def get_details(self) -> str:
        return (self.name, self.email, self.student_id)
