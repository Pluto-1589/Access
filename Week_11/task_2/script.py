import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!


def get_average_grade(path):
    # The function should calculate the average for all the grades in the file and return it as the result. In the above example, calling the function should return 5.75. Return None, if the file does not exist and 0.0 if the file does not contain any grades.

    if not os.path.exists(path):
        return None
    else:
        with open(path, "r") as file:
            content = file.read()

        grades = []

        for line in content.splitlines():
            if line.startswith("#") or not line:
                continue
            else:
                if not ":" in line:
                    pass
                else:
                    name, grade = map(str.strip, line.split(":"))
                try:
                    grades.append(float(grade))
                except ValueError:
                    continue
        print(grade)
        if grades:
            return sum(grades) / len(grades)
        return 0.0


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("HS24/INF/ACCESS/Week_11/task_2/grades.txt"))
