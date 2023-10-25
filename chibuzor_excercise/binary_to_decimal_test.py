from unittest import TestCase
from binary_to_decimal import binary_to_decimal


class TestSomething(TestCase):
    def test_for_the_function_of_binary_to_decimal(self):
        binary_number = 101
        result = binary_to_decimal(binary_number)
        answer = 5
        self.assertEqual(answer, result)

    def test_for_the_function_of_binary_to_decimal2(self):
        binary_number = 101101
        result = binary_to_decimal(binary_number)
        answer = 45
        self.assertEqual(answer, result)

    def test_for_the_function_of_binary_to_decimal3(self):
        binary_number = 110
        result = binary_to_decimal(binary_number)
        answer = 6
        self.assertEqual(answer, result)

    def test_for_the_function_that_convert_binary_to_decimal(self):
        binary_number = 111
        result = binary_to_decimal(binary_number)
        self.assertEqual(result, 7)
