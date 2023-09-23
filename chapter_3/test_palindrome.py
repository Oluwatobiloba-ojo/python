from unittest import TestCase
from .palindrome import is_palindrome


class Test(TestCase):
    def test_is_a_four_digit_number(self):
        number = 34527
        result = is_palindrome(number)

        expected = "not a four digit"

        self.assertEqual(expected, result)

    def test_is_a_palindrome(self):
        number = 1221
        result = is_palindrome(number)
        expected = True
        self.assertEqual(expected, result)
