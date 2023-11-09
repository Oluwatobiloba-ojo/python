from unittest import TestCase
from dictionary import sort


class TestSomethings(TestCase):
    def test_for_a_function_that_sort(self):
        dictionary = {2: 4, 1: 1, 3: 9, 4: 16, 5: 25}
        sorts = sort(dictionary)
        result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertEqual(sorts, result)
