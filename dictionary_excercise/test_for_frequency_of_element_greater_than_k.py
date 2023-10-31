import unittest
from frequency import element_greater_than_k


class MyTestCase(unittest.TestCase):
    def test_something(self):
        k = 2
        lists = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        self.assertEqual(element_greater_than_k(lists, k), [1, 2, 5])

    def test_something_else(self):
        k = 3
        lists = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        self.assertEqual(element_greater_than_k(lists, k), [1, 2])
