import unittest

from self_assesment.sales_calculator_sample import calculate_gross_pay


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = calculate_gross_pay(5000)
        expected = "650.00"
        self.assertEqual(result, expected)

    def test_that_more_than_one_item_and_calculate_gross_pay(self):
        result = calculate_gross_pay(239.99, 129.75, 99.95, 350.89)
        expected = '273.85'
        self.assertEqual(result, expected)
