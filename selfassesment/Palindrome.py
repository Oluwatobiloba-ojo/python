five_Digit = int(input("Enter a five digit number: "))
while five_Digit < 11111 or five_Digit > 99999:
    five_Digit = int(input("Enter a five digit number: "))

first_One = five_Digit // 10000
second_One = five_Digit // 1000 % 10
third_One = five_Digit // 100 % 10
fourth_One = five_Digit // 10 % 10
fifth_One = five_Digit % 10

firstString = str(first_One)
secondString = str(second_One)
thirdString = str(third_One)
fourString = str(fourth_One)
last = str(fifth_One)

add = last + fourString + thirdString + secondString + firstString
reverseFiveDigit = int(add)

if five_Digit == reverseFiveDigit:
    print(f"This {five_Digit} is a palindrome (Saying its the same when reversed)")
else:
    print(f"This is not a palindrome caused the reversed is {reverseFiveDigit}")
