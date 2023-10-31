from unittest import TestCase
from two_list_to_dict import two_list_to_dictionary


class TestSomething(TestCase):
    def test_for_two_list_to_dictionary(self):
        list1 = ['a', 'b', 'c', 'd', 'e']
        list2 = [1, 2, 3, 4, 5]
        self.assertEqual(two_list_to_dictionary(list1, list2), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_for_two_list_to_dictionary2(self):
        list1 = ['a', 'b', 'c', 'd', 'e']
        list2 = [1, 2, 3, 4, 5]
        self.assertEqual(two_list_to_dictionary(list2, list1), {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'})
