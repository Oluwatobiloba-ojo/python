from unittest import TestCase
import Logistics_sample


class Test(TestCase):
    def test_allowance(self):
        payment = Logistics_sample.allowance(50)
        self.assertEqual(15000, payment)

    def test_that_allowance_less_than_50(self):
        payment = Logistics_sample.allowance(60)
        self.assertEqual(20000, payment)

    def test_that_allowance_from_value_less_than_60(self):
        payment = Logistics_sample.allowance(55)
        self.assertEqual(16000, payment)

    def test_for_allowance_for_value_less_than_70(self):
        payment = Logistics_sample.allowance(65)
        self.assertEqual(21250, payment)

    def test_for_allowance_above_70(self):
        payment = Logistics_sample.allowance(75)
        self.assertEqual(42500, payment)