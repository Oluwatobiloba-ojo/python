from unittest import TestCase
import Logistics_sample


class Test(TestCase):
    def test_allowance(self):
        payment = Logistics_sample.allowance(50)
        self.assertEqual(15000, payment)
    def test_that_allowance_from_0_to_50(self):
        payment = Logistics_sample.allowance(60)
        self.assertEqual(20000, payment)
