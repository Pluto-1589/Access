from math import pi

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # [-1, 1, 2, 3]


def square_root_dict(numbers: [int]):
    return {x: x**0.5 for x in numbers}


def even_odd_dict(numbers: [int]):
    """return a dictionary that contains the numbers as keys and for each number 'event' or 'odd' as value"""

    return {n: "even" if n % 2 == 0 else "odd" for n in numbers}


def area_dict(numbers: [int]):
    """numbers as keys and another dictionary as value. The value dictionary shall contain the area of a square with the number as side length, the area of a circle with the number as radius"""

    return {n:
            {
                "square": (n**2),
                "circle": (n**2*pi)
            }
            for n in numbers if n > 0}


def smaller_larger_dict(numbers: [int]):
    """"return a dictionary that has the numbers as keys and another dictionary as value. In this value dictionary every other number is a key and the value tells if the number is 'smaller' or 'larger' as the first key. """
    return {n:
            {
                other: "smaller" if other < n else "larger" for other in numbers if other != n
            }
            for n in numbers}


print(square_root_dict(number_list))
print(even_odd_dict(number_list))
print(area_dict(number_list))
print(smaller_larger_dict(number_list))
