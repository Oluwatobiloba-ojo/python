gallon = float(input("Enter the gallon used (Enter -1 to end: )"))
miles = int(input("Enter miles driven: "))
average = miles / gallon
print(f"The miles and gallon of this tankful is {average:.2f} ")
result = 0
result += average
count = 1
while gallon != -1:
    gallon = float(input("Enter the gallon used (Enter -1 to end: )"))
    miles = int(input("Enter miles driven: "))
    average = miles / gallon
    print(f"The miles and gallon of this tankful is {average:.2f} ")
    result += average
    count += 1
total = result / count
print(f"The overall average of miles and gallon is {total}")

