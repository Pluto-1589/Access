from unittest import TestCase
from script_2 import sort

# == Specification of `sort` ==

# - takes an `Iterable` as a parameter that contains comparable elements
# - sorts all contained elements without changing the original `Iterable`
# - elements should be sorted in ascending order (i.e., smallest first)
# - always returns a new `List` that contains the sorted elements
# - If parameter is `None` or non-iterable, return  `None`.


class SortTests(TestCase):

    def test_sort_integers(self):

        self.assertEqual(sort([3, 1, 2]), [1, 2, 3])

    def test_sort_floats(self):

        self.assertEqual(sort([3.2, 1.1, 2.3]), [1.1, 2.3, 3.2])

    def test_sort_strings(self):

        self.assertEqual(sort(["b", "c", "a"]), ["a", "b", "c"])

    def test_sort_empty(self):

        self.assertEqual(sort([]), [])

    def test_sort_single(self):

        self.assertEqual(sort([2]), [2])

    def test_sort_none(self):

        self.assertEqual(sort(None), None)

    def test_sort_non_iterable(self):

        self.assertEqual(sort(True), None)

    def test_sort_does_not_modify(self):

        original = [3, 1, 2]
        sorted_res = sort(original)
        self.assertEqual(sorted_res, [1, 2, 3])
        self.assertEqual(original, [3, 1, 2])

    def test_sort_with_duplicates(self):

        self.assertEqual(sort([4, 1, 4, 2]), [1, 2, 4, 4])
        self.assertEqual(sort(["b", "a", "b"]), ["a", "b", "b"])
