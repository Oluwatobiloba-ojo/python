import unittest
from sub_sequence import sub_sequence_of_a_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        parent_list = [4, 9, -8, 0, 1, 7, 6]
        sub_list = [9, 1, 7]
        self.assertTrue(sub_sequence_of_a_list(parent_list, sub_list))

    def test_for_the_occurrence_of_a_parent_array(self):
        parent_list = [5, 2, 1, 3, -2, -8, 1]
        sub_list = [3, -8, 1]
        self.assertTrue(sub_sequence_of_a_list(parent_list, sub_list))

    def test_for_the_occurrence_of_a_parent_array2(self):
        parent_list = [5, 2, 1, 3, -2, -8, 1]
        sub_list = [3, -8, 5]
        self.assertFalse(sub_sequence_of_a_list(parent_list, sub_list))
