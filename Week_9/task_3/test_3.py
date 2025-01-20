from unittest import TestCase
from script_3 import median


class MedianTests(TestCase):

    def test_median_median(self):

        self.assertEqual(median([1, 2, 3]), 2)

    def test_median_floats(self):

        self.assertEqual(median([11.20, 3.60, 5.90]), 5.90)

    def test_median_if_even(self):

        self.assertEqual(median([11.20, 5.90]), 8.55)

    def test_median_not_enough_values(self):

        self.assertEqual(median([]), None)

    def test_median_if_one_item(self):

        self.assertEqual(median([2]), 2)
