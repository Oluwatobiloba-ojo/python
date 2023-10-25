from unittest import TestCase
from decimal_to_binary import decimal_to_binary


class TestSomething(TestCase):
    def test_for_conversion_of_decimal_to_binary(self):
        decimal = 5
        result = decimal_to_binary(decimal)
        answer = 101
        self.assertEqual(answer, result)

    def test_for_conversion_of_decimal_to_binary2(self):
        decimal = 6
        result = decimal_to_binary(decimal)
        answer = 110
        self.assertEqual(result, answer)

    def test_for_the_conversion_of_decimal_to_binary3(self):
        decimal = 7
        result = decimal_to_binary(decimal)
        answer = 111
        self.assertEqual(result, answer)

