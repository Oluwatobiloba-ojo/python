from unittest import TestCase

from finanace import Finance


class Test_Case(TestCase):
    def test_for_the_type_of_credit_cards(self):
        number = "4388576018402626"
        card_type = 'Visa cards'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_for_the_type_of_credit_cards_length_must_be_between_13_and_16(self):
        number = "43885760184"
        card_type = 'Invalid input'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_for_the_type_of_credit_cards2(self):
        number = "5388576018402626"
        card_type = 'Master Cards'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_for_the_type_of_credit_cards3(self):
        number = '37388576018402626'
        card_type = 'American Express Cards'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_that_American_Express_Cards_Have_Two_Digit_To_Test_Validity(self):
        number = '3388576018402626'
        card_type = 'Invalid'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_for_the_type_of_credit_cards4(self):
        number = '6388576018402626'
        card_type = 'Discover Cards'
        result = Finance.credit_card_type(number)
        self.assertEqual(card_type, result)

    def test_for_the_validity_status_of_the_credit_card(self):
        number = "4388576018402626"
        card_type = 'Invalid'
        result = Finance.validate_credit_cards(number)
        self.assertEqual(card_type, result)

    def test_for_the_validity_status_of_the_credit_card_2(self):
        number = "5399831619690403"
        card_type = 'Valid'
        result = Finance.validate_credit_cards(number)
        self.assertEqual(card_type, result)

    def test_for_the_validity_status_of_the_credit_card3(self):
        number = "5399831619690404"
        card_type = 'Invalid'
        result = Finance.validate_credit_cards(number)
        self.assertEqual(card_type, result)

    def test_for_the_validity_status_of_the_credit_card4(self):
        number = "234319283049582"
        card_type = 'Invalid'
        result = Finance.validate_credit_cards(number)
        self.assertEqual(card_type, result)

    def test_for_the_validity_status_of_the_credit_card5(self):
        number = "4388576018410707"
        card_type = 'Valid'
        result = Finance.validate_credit_cards(number)
        self.assertEqual(card_type, result)
