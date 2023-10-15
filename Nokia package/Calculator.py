def Calculator():
    stopper = 0
    while stopper != 1:
        print("""
        1 -> Sum
        2 -> Multiply
        3 -> Divide
        4 -> Difference
        """)
        response = int(input("Enter the options you desired: "))
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number "))
        if response == 1:
            print(first_number + second_number)
        elif response == 2:
            print(first_number * second_number)
        elif response == 3:
            if first_number > second_number:
                print(first_number / second_number)
            else:
                print(second_number / first_number)
        elif response == 4:
            if first_number > second_number:
                print(first_number - second_number)
            else:
                print(second_number - first_number)
        stopper = int(input("Enter 1 to stop or enter 0 to continue"))
