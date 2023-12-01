from unittest import TestCase

from Function import palindrome


class TestSomething(TestCase):
    def test_for_that_radar_is_a_palindrome(self):
        inputs = 'radar'
        self.assertTrue(palindrome.isPalindrome(inputs))

    def test_for_that_ada_is_a_palindrome(self):
        inputs = 'ada'
        self.assertTrue(palindrome.isPalindrome(inputs))

    def test_for_that_shop_is_not_a_palindrome(self):
        inputs = 'shop'
        self.assertFalse(palindrome.isPalindrome(inputs))
