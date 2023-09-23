from unittest import TestCase

from Excercises.Account import Account


class TestAccount(TestCase):
    def test_check_balance(self):
        my_account = Account()
        balance = my_account.get_balance()
        self.assertEqual(0, balance)
        my_account.deposit(3000)
        expected = 3000
        result = my_account.get_balance()
        self.assertEqual(result, expected)

    def test_that_we_can_not_deposit_negative_amount(self):
        my_account = Account()
        my_account.deposit(5000)
        my_account.deposit(-4000)
        expected = 5000
        result = my_account.get_balance()
        self.assertEqual(expected, result)

    def test_that_we_can_withdraw_from_an_account(self):
        my_account = Account()
        my_account.deposit(10000)
        my_account.deposit(-4000)
        expected = 10000
        result = my_account.get_balance()
        self.assertEqual(expected, result)

        my_account.withdraw(3000)
        expected = 7000
        result = my_account.get_balance()
        self.assertEqual(expected, result)

    def test_that_we_can_not_withdraw_when_balance_is_less_than_amount(self):
        my_account = Account()
        my_account.deposit(1000)
        my_account.withdraw(20000)
        expected = my_account.get_balance()
        result = 1000
        self.assertEqual(result, expected)

    def test_that_i_can_transfer_from_one_account_to_the_other(self):
        my_account = Account()
        delighted_account = Account()
        delighted_account.deposit(7000)
        my_account.deposit(2000)
        delighted_account.transfer_to(my_account, 3000)
        expected1 = my_account.get_balance()
        result1 = 5000
        expected2 = delighted_account.get_balance()
        result2 = 4000
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

    def test_that_we_can_not_transfer_amount_bigger_than_our_balance(self):
        my_account = Account()
        delighted_account = Account()
        my_account.deposit(2000)
        my_account.transfer_to(delighted_account, 3000)
        expected = my_account.get_balance()
        result1 = 2000
        expected2 = delighted_account.get_balance()
        result2 = 0
        self.assertEqual(expected, result1)
        self.assertEqual(expected2, result2)
