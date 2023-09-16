# Comparing a given integer to another integer

value = int(input("Enter the integer,"
                  "we are to compare with: "))
value2 = int(input("Enter another integer to"
                   "compare with the first integer: "))

if value == value2:
    print(value, "is equal to",  value2)
if value != value2:
    print(value, "is not equals to", value2)
if value > value2:
    print(value,  'is greater than',   value2)
if value < value2:
    print(value, "is less than ", value2)
if value >= value2:
    print(value, "is greater or equal to", value2)
if value <= value2:
    print(value, "is less than or equal to ", value2)
