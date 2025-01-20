
from professor import Professor
from student import Student

# The Course class represents a course offered at the university.


class Course:

    # __init__(): Initializes the course with the given code, name, professor. Also initialize students as an empty list.
    def __init__(self, course_code: str, course_name: str, professor: Professor):
        self.course_code = course_code
        self. course_name = course_name
        self.professor = professor
        self.course = []

    # add_student(): Adds a Student to the course. Returns the total number of students enrolled after adding. Raises a ValueError if the student is already enrolled.
    def add_student(self, student: Student) -> int:

        if student in self.course:
            raise ValueError("Student is already enrolled")
        else:
            self.course.append(student)
            return len(self.course)

    # get_students(): Returns a list of student details for all enrolled students. (Details are obtained by calling get_details() on each student object.)
    def get_students(self) -> list:

        return [student.get_details() for student in self.course]

    # remove_student(): Removes a student from the course by their student_id. Returns the total number of students enrolled after removal. Raises a ValueError if the student is not found.

    def remove_student(self, student_id: str) -> int:

        for student in self.course:
            details = student.get_details()

            for d in details:
                if d == student_id:
                    self.course.remove(student)

            return len(self.course)
        raise ValueError("Student is not found")

    # get_details(): Returns a tuple containing the course details (course_code, course_name, professor_details, number_of_students). (professor_details is obtained by calling get_details() on the professor object.)

    def get_details(self) -> tuple:

        professor_details = self.professor.get_details()
        number_of_students = len(self.course)

        return (self.course_code, self.course_name, professor_details, number_of_students)
