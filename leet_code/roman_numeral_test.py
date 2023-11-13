from unittest import TestCase
from roman_numeral import Solution


class TestSomething(TestCase):
    def test_for_the_roman_numeral_of_4(self):
        result = Solution()
        self.assertEqual("IV", result.intToRoman(4))

    def test_for_the_roman_numeral_of_20(self):
        result = Solution()
        self.assertEqual("XX", result.intToRoman(20))

    def test_for_the_roman_numeral_of_30(self):
        result = Solution()
        self.assertEqual("XXX", result.intToRoman(30))

    def test_for_the_roman_numeral_of_40(self):
        result = Solution()
        self.assertEqual("XL", result.intToRoman(40))

    def test_for_the_roman_numeral_of_98(self):
        result = Solution()
        self.assertEqual("XCVIII", result.intToRoman(98))

    def test_for_the_roman_numeral_of_1040(self):
        result = Solution()
        self.assertEqual('MXL', result.intToRoman(1040))

    def test_for_the_roman_numeral_of_1994(self):
        result = Solution()
        self.assertEqual('MCMXCIV', result.intToRoman(1994))

    def test_for_the_roman_numeral_of_1004(self):
        result = Solution()
        self.assertEqual('LVIII', result.intToRoman(58))
