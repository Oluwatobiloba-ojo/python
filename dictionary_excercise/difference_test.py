from unittest import TestCase
from difference import diff_between_largest_and_smallest


class TestSomething(TestCase):
    def test_for_difference_between_smallest_and_largest(self):
        lists = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(diff_between_largest_and_smallest(lists), 70)
