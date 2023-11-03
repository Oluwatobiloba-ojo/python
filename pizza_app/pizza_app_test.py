from unittest import TestCase
from pizza_main import pizza_box_size_slices, calculate_number_of_slices, calculate_number_of_boxes, \
    calculate_excess_slices, calculate_total_of_pizza


class TestSomething(TestCase):
    def test_for_that_when_i_put_in_big_box_of_pizza_give_me_10_slices(self):
        box_size = "Big"
        self.assertEqual(10, pizza_box_size_slices(box_size))

    def test_for_the_amount_of_slices_in_medium_boxes(self):
        self.assertEqual(6, pizza_box_size_slices("Medium"))

    def test_for_when_they_put_in_size_which_we_dont_have_in_our_app(self):
        self.assertEqual(0, pizza_box_size_slices("Ope"))

    def test_for_when_they_put_in_the_letters_in_different_cases(self):
        self.assertEqual(10, pizza_box_size_slices('biG'))

    def test_for_the_number_of_slices_of_pizza(self):
        self.assertEqual(65, calculate_number_of_slices(10, 10, 5))

    def test_that_number_of_slices_can_not_be_calculated_if_negative(self):
        self.assertEqual(0, calculate_number_of_slices(-39, -55, -67))

    def test_for_no_of_boxes_needed(self):
        self.assertEqual(7, calculate_number_of_boxes(10, 10, 5, "Big"))

    def test_for_number_of_boxes_needed(self):
        self.assertEqual(7, calculate_number_of_boxes(10, 10, 10, "Big"))

    def test_for_no_of_slices_left_after_calculation(self):
        self.assertEqual(5, calculate_excess_slices(10, 10, 5, "Big"))

    def test_for_number_of_slices_when_there_is_no_more(self):
        self.assertEqual(0, calculate_excess_slices(10, 10, 10, "Big"))

    def test_for_number_of_boxes_when_the_size_is_classic(self):
        self.assertEqual(17, calculate_number_of_boxes(10, 10, 5, "small"))

    def test_for_number_of_slices_left_when_the_size_is_classic(self):
        self.assertEqual(3, calculate_excess_slices(10, 10, 5, "Small"))

    def test_for_total_price_of_pizza_with_the_size(self):
        self.assertEqual(35000, calculate_total_of_pizza(10, 10, 5, 'Big'))
