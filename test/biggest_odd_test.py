from unittest import TestCase
from biggest_odd import biggest_odd


class MyTestCase(TestCase):
    def test_something(self):
        number = "23569"
        result = biggest_odd(number)
        answer = "9"
        self.assertEqual(answer, result)

    def test_something2(self):
        self.assertEqual("7", biggest_odd("23457"))
