

def function_message():
    print(""""
        1 -> Write Message
        2 -> Inbox
        3 -> Outbox
        4 -> Picture Message
        5 -> Template
        6 -> Smileys
        7 -> Message Setting
        8 -> Info Service
        9 -> Voice mailBox Number
        10 -> Service Command editor
        11 -> main Menu
        """)
    message = int(input("Enter your response "))
    if message == 1:
        print("Write Message")
    elif message == 2:
        print("Inbox")
    elif message == 3:
        print("OutBox")
    elif message == 4:
        print("Picture Message")
    elif message == 5:
        print("Templates")
    elif message == 7:
        print(""""
            1 -> Set 1
            2 -> Common
            3 -> mainMenu
            4 -> Message
            """)
        setting = int(input("Enter the setting"))
        if setting == 1:
            print(""""
                1 -> Message centre Number
                2 -> Message sent as 
                3 -> Message Validity
                4 -> message
                5 -> main_menu
                """)
            sets = int(input("Enter your response: "))
            if sets == 1:
                print("Message centre Number")
            elif sets == 2:
                print("Message sent as ")
            elif sets == 3:
                print("Message Validity")
            elif sets == 3:
               pass
               # main_menu()
            elif sets == 4:
                function_message()
        elif setting == 2:
            print("""
                1 -> Delivery Report
                2 -> Reply Via Same Centre
                3 -> Character Support
                4 -> Message
                5 -> main_menu
                """)
            common = int(input("Enter your response: "))
            if common == 1:
                print("Delivery Report: ")
            elif common == 2:
                print("Reply Via Same Centre")
            elif common == 3:
                print("Character Support")
            elif common == 4:
                function_message()
            elif common == 5:
                pass
                # main_menu()
    elif message == 8:
        print("Info service")
    elif message == 9:
        print("Voice mail Box number")
    elif message == 10:
        print("Service Command Editor")
    elif message == 11:
        pass
        # main_menu()
