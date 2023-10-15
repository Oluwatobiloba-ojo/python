from unittest import TestCase

from self_assesment import Triple_of_each_element


class MyTestCase(TestCase):
    def test_that_an_element_can_be_tripled(self):
        number = [3, 7, 2, 6, 5]
        answer = [27, 343, 8, 216, 125]
        result = Triple_of_each_element.triple(number)
        self.assertEqual(answer, result)
