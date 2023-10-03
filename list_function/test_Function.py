from unittest import TestCase

from list_function.Function import largest, reverse, check_element, odd_position, even_position, running_total, \
    is_palindrome, sum_for_loop, sum_while_loop, concatenate_lists, combines_two_list, convert_to_list


class Test(TestCase):
    def test_largest_element_in_a_list(self):
        number = [1, 4, 5, 6, 7, 8, 9, 10]
        result = largest(number)
        answer = 10
        self.assertEqual(result, answer)

    def test_largest_element_in_a_list2(self):
        number = [10, 20, 40, 60, 90, 1, 500]
        result = largest(number)
        answer = 500
        self.assertEqual(answer, result)

    def test_the_reverse_of_a_list(self):
        number = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = reverse(number)
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, answer)

    def test_reverse_of_a_list_2(self):
        number = [10, 20, 40, 60, 90, 1, 500]
        result = reverse(number)
        answer = [500, 1, 90, 60, 40, 20, 10]
        self.assertEqual(result, answer)

    def test_whether_an_element_is_in_a_list(self):
        number = [1, 2, 4, 6, 7, 8, 9]
        element = 10
        result = check_element(number=number, element=element)
        self.assertFalse(result)

    def test_whether_an_element_is_present_in_a_list(self):
        number = [1, 4, 6, 8, 9, 2]
        element = 2
        result = check_element(number=number, element=element)
        self.assertTrue(result
                        )

    def test_that_an_element_is_in_a_list(self):
        numbers = [10, 4, 5, 2, 1]
        element = 1
        result = check_element(numbers, element)
        self.assertTrue(result)

    def test_for_the_odd_position_in_a_list(self):
        numbers = [10, 3, 4, 5, 6, 7]
        answer = [3, 5, 7]
        result = odd_position(numbers)
        self.assertEqual(result, answer)

    def test_for_the_odd_position(self):
        numbers = [2, 2, 3, 4, 5, 8, 7, 10]
        answer = [2, 4, 8, 10]
        result = odd_position(numbers)
        self.assertEqual(result, answer)

    def test_for_evenly_place_position_in_a_list(self):
        numbers = [2, 3, 5, 6, 7, 9]
        answer = [2, 5, 7]
        result = even_position(numbers)
        self.assertEqual(answer, result)

    def test_for_evenly_place_position_in_a_list2(self):
        numbers = [2, 5, 6, 7, 7, 8, 9, 0, 10]
        answer = [2, 6, 7, 9, 10]
        result = even_position(number=numbers)
        self.assertEqual(result, answer)

    def test_for_a_function_that_compute_the_total_of_the_list(self):
        numbers = [1, 5, 7, 8, 2]
        answer = 1 + 5 + 7 + 8 + 2
        result = running_total(numbers)
        self.assertEqual(result, answer)

    def test_something_total(self):
        numbers = [2, 5, 7, 90, -1]
        answer = (2 + 5 + 7 + 90) - 1
        result = running_total(numbers)
        self.assertEqual(result, answer)

    def test_that_a_string_is_a_palindrome(self):
        name = "dad"
        result = is_palindrome(name)
        self.assertTrue(result)

    def test_for_a_string_in_a_palindrome(self):
        name = "mums"
        result = is_palindrome(name)
        self.assertFalse(result)

    def test_for_the_sum_of_a_list_with_a_for_loop(self):
        numbers = [1, 4, 6, 7, 8, 9, 10]
        result = sum_for_loop(numbers)
        answer = 1 + 4 + 6 + 7 + 8 + 9 + 10
        self.assertEqual(result, answer)

    def test_for_the_sum_of_a_list_using_a_while_loop(self):
        numbers = [1, 4, 6, 7, 8, 9, 10]
        result = sum_while_loop(numbers)
        answer = 1 + 4 + 6 + 7 + 8 + 9 + 10
        self.assertEqual(result, answer)

    def test_for_sum_of_a_list_using_while_loop_and_using_for_loop(self):
        numbers = [1, 4, 6, 7, 8, 9, 10]
        result = sum_while_loop(numbers)
        result2 = sum_for_loop(numbers)
        answer = 1 + 4 + 6 + 7 + 8 + 9 + 10
        self.assertEqual(result, answer)
        self.assertEqual(result2, answer)

    def test_for_function_that_concatenate_a_list_with_a_list(self):
        characters = ['a', 'b', 'c']
        integers = [1, 2, 3, 4]
        answer = ['a', 'b', 'c', 1, 2, 3, 4]
        result = concatenate_lists(integers, characters)
        self.assertEqual(result, answer)

    def test_for_function_that_join_list_and_list_together(self):
        number = [1.0, 2.0, 2.5, 3.0]
        integers = [1, 3, 5]
        result = concatenate_lists(number, integers)
        answer = [1, 3, 5, 1.0, 2.0, 2.5, 3.0]
        self.assertEqual(result, answer)

    def test_for_function_that_takes_an_element_from_different_list(self):
        number = [1, 2, 3, 4, 5, 7, 8, 9]
        character = ['a', 'b', 'c', 'd', 'e', 'f']
        answer = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 7, 'f', 8, 9]
        result = combines_two_list(number, character)
        self.assertEqual(answer, result)

    def test_for_function_that_takes_an_element_from_different_list2(self):
        number = [1, 2, 3, 4, 5, 7, 8, 9]
        character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j']
        answer = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 7, 'f', 8, 'g', 9, 'i', 'j']
        result = combines_two_list(number, character)
        self.assertEqual(answer, result)

    def test_for_a_function_that_takes_in_a_number_and_return_as_list(self):
        number = 23456
        answer = [2, 3, 4, 5, 6]
        result = convert_to_list(number)
        self.assertEqual(answer, result)

    def test_that_an_integer_can_be_converted_into_a_list(self):
        numbers = 23456897
        answer = [2, 3, 4, 5, 6, 8, 9, 7]
        result = convert_to_list(numbers)
        self.assertEqual(result, answer)
