from unittest import TestCase

from Assesment.check_element import check_element


class TestSomething(TestCase):

    def test_whether_an_element_exist_in_a_list(self):
        lists = [1, 5, 8, 3]
        element = 3
        result = check_element(lists, element)
        self.assertTrue(result)

    def test_whether_an_element_does_not_exist_in_a_list(self):
        lists = [1, 5, 8, 3]
        element = -1
        result = check_element(lists, element)
        self.assertFalse(result)

    def test_for_an_element_zero_is_not_in_a_list(self):
        lists = [1, 5, 8, 3]
        element = 0
        result = check_element(lists, element)
        self.assertFalse(result)