from unittest import TestCase
from Binary_Digit import binary_convert


class MyTestCase(TestCase):
    def test_something(self):
        binary_value = 111
        result = binary_convert(binary_value)
        answer = 7.0
        self.assertEqual(result, answer)

    def test_somethings(self):
        binary_value = 11
        result = binary_convert(binary_value)
        answer = 3
        self.assertEqual(result, answer)

    def test_somethings2(self):
        binary_value = 101
        result = binary_convert(binary_value)
        answer = 5
        self.assertEqual(result, answer)

    def test_Something3(self):
        binary_value = 11111111
        result = binary_convert(binary_value)
        answer = 255
        self.assertEqual(result, answer)

    def test_something3(self):
        binary_value = 1111
        result = binary_convert(binary_value)
        answer = 15
        self.assertEqual(result, answer)
