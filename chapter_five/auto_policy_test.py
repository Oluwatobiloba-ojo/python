from unittest import TestCase
from auto_policy import auto_policy


class TestSomething(TestCase):
    def test_that_auto_policy_has_attributes(self):
        auto = auto_policy()
        account = 111111
        auto.set_account_number(account)
        self.assertEqual(auto.get_auto_policy(), account)
        model = 'Camry'
        auto.set_make_model(model)
        self.assertEqual(model, auto.get_make_model())

    def test_that_auto_policy_has_state(self):
        auto = auto_policy()
        state = 'Nigeria'
        auto.setstate(state)
        self.assertEqual(auto.get_state(), state)

    def test_that_state_put_in_has_auto_policy(self):
        auto = auto_policy()
        state = 'New York'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())

    def test_that_nigeria_is_a_fault_state_which_has_no_policy(self):
        auto = auto_policy()
        state = 'nigeria'
        auto.setstate(state)
        self.assertFalse(auto.is_no_fault_state())

    def test_that_new_jersey_is_nor_a_fault_state_which_means_it_has_policy(self):
        auto = auto_policy()
        state = 'new jersey'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())

    def test_for_that_new_hampshire_is_a_no_fault_state_which_is_it_has_policy(self):
        auto = auto_policy()
        state = 'New Hampshire'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())

    def test_that_Connecticut_is_a_state_which_posses_policy(self):
        auto = auto_policy()
        state = 'Connecticut'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())

    def test_for_that_vermont_is_a_state_which_posses_policy(self):
        auto = auto_policy()
        state = 'Vermont'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())

    def test_for_that_a_maine_is_a_state_which_has_account_policy(self):
        auto = auto_policy()
        state = 'Pennsylvania'
        auto.setstate(state)
        self.assertTrue(auto.is_no_fault_state())