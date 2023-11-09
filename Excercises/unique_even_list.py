from unittest import TestCase
from unique_even import even_list


class TestSomething(TestCase):
    def test_for_unique_element(self):
        lists = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
        expected = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual(expected, even_list(lists))
