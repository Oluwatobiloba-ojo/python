gallon = float(input("Enter the gallon used: "))
miles = int(input("Enter miles driven: "))
average = miles / gallon
print(f"The miles and gallon of this tankful is {average:.2f} ")
milesTotal = 0
milesTotal += miles
gallonTotal = 0
gallonTotal += gallon
flag_value = int(input("Enter -1 to end and number greater than 1 to continue"))
while flag_value != -1:
    gallon = float(input("Enter the gallon used (Enter -1 to end: )"))
    miles = int(input("Enter miles driven: "))
    gallonTotal += gallon
    milesTotal += miles
    average = miles / gallon
    print(f"The miles and gallon of this tankful is {average:.2f} ")
    flag_value = int(input("Enter -1 to end and number greater than 1 to continue"))
total = milesTotal / gallonTotal
print(f"The overall average of miles and gallon is {total:.6f}")
