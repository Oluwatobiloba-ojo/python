from unittest import TestCase
from strings import removal_of_empty_string


class TestSomethings(TestCase):
    def test_for_removal_of_empty_strings(self):
        string_list = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        self.assertEqual(removal_of_empty_string(string_list), ['ABC', 'xyz', 'abc', 'XYZ'])

    def test_for_removal_of_empty_strings2(self):
        string_list = ['', 'ABC', 'xyz', '', 'abc', 'XYZ', '', '123']
        self.assertEqual(removal_of_empty_string(string_list), ['ABC', 'xyz', 'abc', 'XYZ', '123'])
