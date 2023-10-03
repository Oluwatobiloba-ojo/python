def CallRegister():
    print("""
        1 -> Missed Calls
        2 -> Received Calls
        3 -> Dialled Number
        4 -> Erase Recent Call List
        5 -> Show call Duration
        6 -> Show call Cost
        7 -> Call cost setting
        8 -> Prepaid Credit
        9 -> main_menu
        """)
    call = int(input("Enter your response:"))
    if call == 1:
        print("Missed Calls")
    elif call == 2:
        print("Received calls")
    elif call == 3:
        print("Dialled Number")
    elif call == 4:
        print("Erase Recent Call list")
    elif call == 5:
        print("""
            1 -> Last Call Duration
            2 -> All Calls Duration
            3 -> Received Call Duration
            4 -> Dialled Call Duration
            5 -> Clear's timer
            6 -> Call_Register
            7 -> main_menu
            """)
        duration = int(input("Enter your response: "))
        if duration == 1:
            print("Last call duration")
        elif duration == 2:
            print("All calls duration")
        elif duration == 3:
            print("Received call duration")
        elif duration == 4:
            print("Dialled Call Duration")
        elif duration == 5:
            print("Clear's timer")
        elif duration == 6:
            CallRegister()
        elif duration == 7:
            pass
            # main_menu()
    elif call == 6:
        print("""
            1 -> Last Call Cost
            2 -> All Call Cost
            3 -> Clear Counter
            4 -> Call Register
            5 -> main_menu
            """)
        cost = int(input("Enter the options: "))
        if cost == 1:
            print("Last Call Cost")
        elif cost == 2:
            print("All Call Cost")
        elif cost == 3:
            print("Clear counter")
        elif cost == 4:
            CallRegister()
        elif cost == 5:
            pass
            # main_menu()
    elif call == 7:
        print("""
        1 -> Call Cost Limit
        2 -> Show Cost in
        3 -> Call Register
        4 -> main_menu
        """)
        cost = int(input("Enter the response: "))
        if cost == 1:
            print("Call Cost Limit: ")
        elif cost == 2:
            print("Show Cost in ")
        elif cost == 3:
            CallRegister()
        elif cost == 4:
            pass
            # main_menu()
    elif call == 8:
        print("Prepaid Credit")
    elif call == 9:
        pass
        # main_menu()


def Clock():
    print("""
    1 -> Alarm Clock
    2 -> Clock Setting
    3 -> Data Setting
    4 -> Stopwatch
    5 -> Count down timer
    6 -> Auto update of date and time
    """)
    clock = int(input("Enter your response: "))
    if clock == 1: print("Alarm clock")
    elif clock == 2: print("Clock setting")
    elif clock == 3: print("Date Setting")
    elif clock == 4: print('Stop watch')
    elif clock == 5: print("Count down timer")
    elif clock == 6: print("Auto update of time and date")