from unittest import TestCase
from script_1 import sorted_arrays_overlap

# sorted_arrays_overlap takes two arrays as parameters and retrieves elements that are present in both arrays.


class SortedArraysOverlapTest(TestCase):
    # A correct implementation of sorted_arrays_overlap must comply with the following requirements:

    # Input:

    # The function takes two parameters called array_1 and array_2:

    # These arrays are non-empty lists of any integers sorted in ascending order.
    def test_non_empty_lst(self):

        input_array_1 = [-5, -3, -1, 7, 8, 14, 19]
        input_array_2 = [-8, -5, -2, -1, 19]

        expected_output = [-5, -1, 19]
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(expected_output, actual_output)

    def test_non_empty_constraint(self):

        input_array_1 = []
        input_array_2 = [-8, -5, -2, -1, 19]

        with self.assertRaises(ValueError, msg="Expected ValueError when the first array is empty."):
            sorted_arrays_overlap(input_array_1, input_array_2)

        input_array_1 = [-8, -5, -2, -1, 19]
        input_array_2 = []

        with self.assertRaises(ValueError, msg="Expected ValueError when the second array is empty."):
            sorted_arrays_overlap(input_array_1, input_array_2)

        input_array_1 = []
        input_array_2 = []

        with self.assertRaises(ValueError, msg="Expected ValueError when both arrays are empty."):
            sorted_arrays_overlap(input_array_1, input_array_2)

    def test_non_integers(self):

        input_array_1 = ["not", "an", "integer", "list", "."]
        input_array_2 = [-8, -5, -2, -1, 19]

        # expected_output = "Both lists must only contain integers!"
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        with self.assertRaises(TypeError):
            actual_output

    def test_integers(self):

        input_array_1 = [-5, -3, -1, 7, 8, 14, 19]
        input_array_2 = [-8, -5, -2, -1, 19]

        # expected_output = [-5, -1, 19]
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        for output in actual_output:
            self.assertIsInstance(output, int)

    def test_ascending_order(self):

        input_array_1 = [-5, -3, -1, 7, 8, 14, 19]
        input_array_2 = [-8, -5, -2, -1, 19]

        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, sorted(actual_output))

    def test_unordered(self):

        input_array_1 = [-1, 7, -5, -3, 8, 14, 19]
        input_array_2 = [-8, -5, 19, -2, -1,]

        with self.assertRaises(ValueError, msg="Expected ValueError when the first array is not sorted."):
            sorted_arrays_overlap(input_array_1, input_array_2)

        # Test case where the second array is unordered
        input_array_1 = [-8, -5, -2, -1, 19]  # Sorted
        input_array_2 = [19, -8, -1, -5, -2]  # Unsorted

        with self.assertRaises(ValueError, msg="Expected ValueError when the second array is not sorted."):
            sorted_arrays_overlap(input_array_1, input_array_2)

        # Test case where both arrays are unordered
        input_array_1 = [-1, 7, -5, -3, 8, 14, 19]  # Unsorted
        input_array_2 = [19, -8, -1, -5, -2]  # Unsorted

        with self.assertRaises(ValueError, msg="Expected ValueError when both arrays are not sorted."):
            sorted_arrays_overlap(input_array_1, input_array_2)

#########################################

    #     Output:

    # The function returns:
    def test_input_types(self):
        # a string Invalid input types! Both parameters should be arrays. if either of the arguments is not of type list.

        input_array_1 = "not a list"
        input_array_2 = [-8, -5, 19, -2, -1,]

        expected_output = "Invalid input types! Both parameters should be arrays."
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output)

    def test_empty_arrays(self):
        # a string Empty arrays! Neither of the arrays can be empty. if either of the arguments is an empty list.

        input_array_1 = []
        input_array_2 = [-8, -5, 19, -2, -1,]

        expected_output = "Empty arrays! Neither of the arrays can be empty."
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output)

    def test_invalid_data_type(self):
        # a string Invalid data types within arrays! Arrays should contain only integers. if either of the passed lists contains non-integer elements.

        input_array_1 = ["invalid", "data", "type", "here"]
        input_array_2 = [-8, -5, 19, -2, -1,]

        expected_output = "Invalid data types within arrays! Arrays should contain only integers."
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output)

    def test_not_sorted_arrays(self):
        # a string Not sorted arrays! Both arrays should be sorted in ascending order. if either of the passed lists is not sorted in ascending order.

        input_array_1 = [-1, 7, -5, -3, 8, 14, 19]
        input_array_2 = [19, -8, -1, -5,  -2]

        expected_output = "Not sorted arrays! Both arrays should be sorted in ascending order."
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output)

    def test_no_overlap(self):
        # a string There are no overlapping elements in given arrays. if there are no same elements in the arrays.

        input_array_1 = [1, 2, 3]
        input_array_2 = [4, 5, 6]

        expected_output = "There are no overlapping elements in given arrays."
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output)

    def test_intersection(self):
        # a list containing elements that represent an intersection of the two arrays if the arguments passed to a function are valid.

        input_array_1 = [1, 2, 3, 4, 5]
        input_array_2 = [2, 3, 4, 5, 6]

        expected_output = [2, 3, 4, 5]
        actual_output = sorted_arrays_overlap(input_array_1, input_array_2)

        self.assertEqual(actual_output, expected_output), "Function is valid"
