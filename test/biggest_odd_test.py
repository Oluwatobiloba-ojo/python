from unittest import TestCase

from snacks.Corn_flakes import equal_string
from snacks.biggest_odd import biggest_odd


class MyTestCase(TestCase):
    def test_something(self):
        number = "23569"
        result = biggest_odd(number)
        answer = "9"
        self.assertEqual(answer, result)

    def test_something2(self):
        self.assertEqual("7", biggest_odd("23457"))

    def test_equal_strings(self):
        string2 = "Love"
        string = "evol"
        self.assertTrue(equal_string(string2, string))

    def test_equal_strings2(self):
        string = "loveei"
        string2 = "evolve"
        self.assertFalse(equal_string(string, string2))

    def test_equal_string3(self):
        string = "tie"
        string2 = "ban"
        self.assertFalse(equal_string(string,string2))
