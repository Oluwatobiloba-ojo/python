from unittest import TestCase
from roasted_corn import character_frequency


class TestSomething(TestCase):
    def test_for_character_frequency(self):
        sample = "google.com"
        result = character_frequency(sample)
        expected = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(result, expected)

    def test_for_character_frequency2(self):
        sample = "tobi"
        result = character_frequency(sample)
        expected = {'t': 1, 'o': 1, 'b': 1, 'i': 1}
        self.assertEqual(result, expected)

    def test_for_the_character_for_frequency3(self):
        sample = 'ope'
        result = character_frequency(sample)
        expected = {'o': 1, 'p': 1, 'e': 1}
        self.assertEqual(result, expected)
