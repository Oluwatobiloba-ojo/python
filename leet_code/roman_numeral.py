class Solution(object):
    def range_check(self, roman_constant, number):
        value = 0
        for key in roman_constant.keys():
            if number < key:
                return value
            value = key
        return value

    def intToRoman(self, number):
        result = ''
        roman_constant = {1: "I", 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                          500: 'D', 900: 'CM', 1000: 'M'}
        while number != 0:
            if number in roman_constant.keys():
                result += roman_constant[number]
                number -= number
            else:
                range_key = self.range_check(roman_constant, number)
                number -= range_key
                result += roman_constant[range_key]
        return result
