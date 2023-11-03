from unittest import TestCase
from string_beautifying import beautify


class TestSomething(TestCase):
    def test_for_addition_of_a_ing_to_a_string_which_their_is_no_ing_there(self):
        inputs = 'abc'
        self.assertEqual('abcing', beautify(inputs))

    def test_that_if_the_string_already_contain_ing_should_add_ly(self):
        inputs = 'sting'
        self.assertEqual('stingly', beautify(inputs))

    def test_for_if_the_length_is_two_and_its_not_three(self):
        inputs = 'it'
        self.assertEqual(inputs, beautify(inputs))

    def test_if_it_already_have_ing_and_ly_should_not_do_so(self):
        inputs = 'stingly'
        self.assertEqual(inputs, beautify(inputs))
