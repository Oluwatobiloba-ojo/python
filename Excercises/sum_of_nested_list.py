from unittest import TestCase
from sum_list import sum_list


class TestSomething(TestCase):
    def test_for_sum_of_a_nested_list(self):
        lists = [[2, 4, 5, 6], [2, 3, 5, 6]]
        sums_of = 33
        self.assertEqual(sums_of, sum_list(lists))
