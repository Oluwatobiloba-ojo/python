from unittest import TestCase
from element_to_the_end import element_to_the_end


class TestSomething(TestCase):
    def test_that_element_2_in_the_list_will_move_to_the_end_of_list(self):
        list_of_numbers = [2, 1, 2, 2, 2, 3, 4, 2]
        element = 2
        self.assertEqual([1, 3, 4, 2, 2, 2, 2, 2], element_to_the_end(list_of_numbers, element))
