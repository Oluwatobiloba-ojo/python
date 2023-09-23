stopper = int(input("Enter 1 to continue (Enter 0 to cancel)"))
while stopper != 0:
    theName = input("Enter your name: ")
    item = int(input("Enter the number of items you you did in a week: "))
    if item > 1:
        total = 0
        for constant in range(1,item+1):
            value = int(input("Enter the value of each item: "))
            total += value
        basePay = 200
        percentage = 0.09
        result1 = percentage * total
        result2 = basePay + result1
        print(f"{theName} earning is {result2}")
    else:
        value = int(input("Enter the value of the item: "))
        basePay = 200
        percentage = 0.09
        answer = percentage * value
        result = answer + basePay
        print(f"{theName} earning is {result}")
    stopper = int(input("Enter 1 to continue (Enter 0 to stop program)"))