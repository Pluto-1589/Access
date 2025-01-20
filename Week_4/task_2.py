def square_numbers(numbers):
    '''this one just serves as an example'''
    return [number ** 2 for number in numbers]


def even_numbers(numbers):
    """returns a list of all numbers from numbers which are even. The resulting list should be a subset of the original list."""

    return [num for num in numbers if num % 2 == 0]


def all_even(numbers):
    from math import ceil
    """return a list which converted all odd numbers to the closest even number (towards positive infinity) and leave the already even numbers untouched. For this function you only need to consider the set of positive real numbers. The lengths of the original list and the resulting list should be equal.
    
    all_even(numbers) should return a list which converted all numbers to the closest even number. Use the following strategy: round the value. If the rounded value is odd, add 1 to the value and round it again (this will result in an even number). The lengths of the original list and the resulting list should be equal."""

    # return [num + 1 if num % 2 != 0 else num for num in numbers]

    # from math import ceil

    # return [ceil(num) + 1 if isinstance(num, float) and ceil(num) % 2 != 0 else ceil(num) if isinstance(num, float) else num + 1 if num % 2 != 0 else num for num in numbers]

    # return [round(num) + 1 if isinstance(num, float) and round(num) % 2 != 0 else num + 1 if num % 2 != 0 ]

    return [
        round(num) + 1 if isinstance(num, float) and round(num) % 2 != 0
        else round(num) if isinstance(num, float)
        else num + 1 if num % 2 != 0
        else num
        for num in numbers
    ]


def only_integers(numbers):
    """returns only integers"""
    return [num for num in numbers if isinstance(num, int)]


def only_positive(numbers):
    """return a list where all the numbers from numbers have been converted to positive. The resulting list and the original list should have the same length."""

    return [num + (-num*2) if num < 0 else num for num in numbers]


def from_1_to_1000_containing_a(a):
    # return a list of all numbers up to a thousand that somewhere contain the number a. example: from_1_to_1000_containing_a(2) => [2, 12, 20, ...].

    return [num for num in range(0, 1001) if str(a) in str(num)]


def multiple_of_a_and_greater_than_b(numbers, a, b):
    """contain all the numbers from numbers that are a multiple of a and greater than b."""

    return [num for num in numbers if num % a == 0 and num > b]


num_lst = [1, 2, 3, 6, 7, 8, 9, ]
neg_num_lst = [-1, -2, 6, -7, -8, -9]
float_lst = [1.1, 2.2, 3.4, 1.5, 6, 7, 8, 9]


# print(square_numbers(num_lst))
# print(even_numbers(num_lst))
print(all_even(float_lst))
# print(only_integers(float_lst))
# print(only_positive(num_lst))
# print(from_1_to_1000_containing_a(7))
# print(multiple_of_a_and_greater_than_b(num_lst, 3, 4))
