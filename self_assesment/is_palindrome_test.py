from unittest import TestCase
from Is_Pallindrome import is_palindrome


class TestCases(TestCase):
    def test_if_number_is_palindrome(self):
        result = is_palindrome(12321)
        self.assertTrue(result)

    def test_if_number_is_palindrome2(self):
        result = is_palindrome(121)
        self.assertTrue(result)

    def test_is_palindrome(self):
        result = is_palindrome(12345)
        self.assertFalse(result)

    def test_is_palindrome2(self):
        result = is_palindrome(12221)
        self.assertTrue(result)