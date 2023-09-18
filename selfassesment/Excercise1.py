number = int(input("Enter a number: "))
addition = 0
count = 0
while count != 11:
    if number > 0:
        addition += number
        number = int(input("Enter a number: "))
        print(f"sum is  {addition}")
        count += 1

