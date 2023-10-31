from unittest import TestCase
from extremes import extremes


class TestSomething(TestCase):
    def test_for_the_minimum_and_maximum_addition(self):
        numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]
        result = 11
        self.assertEqual(result, extremes(numbers))

    def test_for_the_minimum_add_of_maximum_addition(self):
        numbers = [1, 3, 4, 5, 6, 100, 50]
        result = 101
        self.assertEqual(result, extremes(numbers))
