from unittest import TestCase
from number_of_characters_in_dict import count_character


class TestSomething(TestCase):
    def test_that_for_number_of_each_character_in_a_string(self):
        value: str = "semicolon.africa"
        result: dict = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(result, count_character(value))

    def test_that_for_the_number_of_string_value_mosquito(self):
        value: str = 'mosquito'
        result: dict = {'m': 1, 'o': 2, 's': 1, 'q': 1, 'u': 1, 'i': 1, 't': 1}
        self.assertEqual(result, count_character(value))
