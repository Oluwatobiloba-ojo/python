taxRate = 0
for count in range(3):
    theName = input("Enter your name: ")
    salary = int(input("Enter the salary Paid for the month"))
    if salary <= 30000:
        taxRate = 0.15 * salary
    else:
        taxRate = 0.20 * salary
    print(f"The name is {theName} and the tax rate is {taxRate}")