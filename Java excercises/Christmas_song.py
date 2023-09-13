age = int(input("Enter your age: "))
match age // 10:
    case 1:
        print("You are not eligible")
    case 2:
        print("You are eligible cause you are between age 20 to 29")
    case 3:
        print("You are eligible cause you are between age 30 to 39")
    case 4:
        print("You are over eligible cause you are between age 40 to 49")
    case _:
        print("You are beyond this age bracket")
