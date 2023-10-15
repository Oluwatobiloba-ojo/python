def Add_name():
    lists = []
    stopper = 0
    while stopper != 1:
        number = input("Enter the person phoneNumber: ")
        lists.append(number)
        stopper = int(input("Enter 1 to stop or enter 0 to continue: "))
    print(lists)

