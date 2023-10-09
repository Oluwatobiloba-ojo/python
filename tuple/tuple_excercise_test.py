from unittest import TestCase

from tuple import tuple_


class TestTuple(TestCase):
    def test_that_a_tuple_can_be_reversed(self):
        number = (10, 20, 30, 40, 50,)
        results = tuple_.reverse(number)
        result = (50, 40, 30, 20, 10)
        self.assertEqual(results, result)

    def test_for_a_function_that_brings_out_a_particular_element_and_and_their_indices(self):
        tuples = ("Orange", (10, 20, 30), (5, 15, 25))
        result = tuple_.check_element(tuples)
        answer = ((0, 20), (1, 25))
        self.assertEqual(result, answer)

    def test_that_a_tuple_can_be_unpack_and_return_as_tuple(self):
        tuple3 = 15, 25, 60, 50, 30, 40, 45, 55
        answer = (55, 15)
        result = tuple_.unpack(tuple3)
        self.assertEqual(answer, result)

    def test_that_a_nested_tuple_can_jump_by_two_terms(self):
        tuple4 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
        answer = (('c', 11), ('a', 23), ('d', 29), ('b', 37))
        result = tuple_.swap_indices_element(tuple4)
        self.assertEqual(result, answer)

    def test_for_the_output_of_duplicate_value_in_the_tuple(self):
        tuple5 = 20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5
        answer = 5, 10, 20
        result = tuple_.duplicate(tuple5)
        self.assertEqual(answer, result)
