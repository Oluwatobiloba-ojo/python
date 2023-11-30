from unittest import TestCase

from valid_parenthese import isValids


class TestSomething(TestCase):
    def test_for_that_validation_of_a_parentheses(self):
        value = '()'
        self.assertTrue(isValids(value))

    def test_for_the_validation_of_a_wrong_parentheses(self):
        value = '(}'
        self.assertFalse(isValids(value))

    def test_for_the_validation_of_a_right_parentheses(self):
        value = '()[]{}'
        self.assertTrue(isValids(value))

    def test_for_the_validation_of_a_wrong_parentheses_of_this(self):
        value = '(){}[}'
        self.assertFalse(isValids(value))

    def test_for_the_validation_of_right_parentheses(self):
        value = '{}()[](){]'
        self.assertFalse(isValids(value))

    def test_for_the_validation_of_a_right_parentheses1(self):
        value = '(([]()()){})'
        self.assertTrue(isValids(value))

    def test_for_the_validation_of_wrong_parentheses(self):
        value = '(){}#[]'
        self.assertFalse(isValids(value))
