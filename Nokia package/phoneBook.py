from Add_name import Add_name


def phoneBook():
    print("""
        1 -> Search
        2 -> Service Nos
        3 -> Add name
        4 -> Erase
        5 -> Edit
        6 -> Assign Tone
        7 -> Send b' cards
        8 -> Options
        9 -> Speed Dials
        10 -> Voice tags
        11 -> main Menu
        """)
    response = int(input("Enter the options: "))
    if response == 1:
        print("Search")
    elif response == 2:
        print("Service Nos")
    elif response == 3:
        Add_name()
    elif response == 4:
        print("Erase ")
    elif response == 5:
        print("Edit")
    elif response == 6:
        print("Assign tone")
    elif response == 7:
        print("Send b' cards")
    elif response == 8:
        print("""
            1 -> Type of view
            2 -> Memory Status
            3 -> main_menu
            """)
        option = int(input("Enter your option"))
        if option == 1:
            print("Type of view ")
        elif option == 2:
            print("Memory Status")
        elif option == 3:
            pass
            # main_menu()
    elif response == 9:
        print("Speed Dials")
    elif response == 10:
        print("Voice tags")
    elif response == 11:
        pass
        # main_menu()
