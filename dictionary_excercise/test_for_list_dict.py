from unittest import TestCase
from list_to_dict import list_to_dictionary


class TestSomething(TestCase):
    def test_for_list_to_dictionary(self):
        lists = ['apple', 'banana', 'coconut']
        self.assertEqual(list_to_dictionary(lists), {'a': 'apple', 'b': 'banana', 'c': 'coconut'})

    def test_for_list_to_dictionary2(self):
        lists = ['apple', 'banana', 'coconut', 'corn']
        self.assertEqual(list_to_dictionary(lists), {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'})

    def test_for_list_to_dictionary3(self):
        lists = ['apple', 'banana', 'coconut', 'coconut']
        self.assertEqual(list_to_dictionary(lists), {'a': 'apple', 'b': 'banana', 'c': 'coconut'})
