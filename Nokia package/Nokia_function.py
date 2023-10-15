def Tones():
    print("""
    1 -> Ringing Tone
    2 -> Ringing volume
    3 -> Incoming call alert
    4 -> Composer
    5 -> Message Alert zone
    6 -> KeyPad Tone
    7 -> Warning and Game Tone
    8 -> Vibrating Alert
    9 -> Screen Saver
    10 -> main_menu
    """)
    tones = int(input("Enter the response:"))
    if tones == 1:
        print("Ringing Tone")
    elif tones == 2:
        print("Ringing Volume")
    elif tones == 3:
        print("Incoming call alert")
    elif tones == 4:
        print("Composer")
    elif tones == 5:
        print("Message Alert zone")
    elif tones == 6:
        print("Keypad Tone")
    elif tones == 7:
        print("Warning and Game Tone")
    elif tones == 8:
        print("Vibrating Alert")
    elif tones == 9:
        print("Screen Saver")
    elif tones == 10:
        pass
        # main_menu()


def Setting():
    print("""
        1 -> Call Setting
        2 -> Phone Setting
        3 -> Security Setting
        4 -> Restore Factory Setting
        """)
    setting = int(input("Enter your response: "))
    if setting == 1:
        print("""
            1 -> Automatic redial
            2 -> Speed Dialling
            3 -> Call Waiting Option
            4 -> Own Number Sending
            5 -> Phone line in use
            6 -> Automatic answer
            """)
        callS = int(input("Enter your response:"))
        if callS == 1:
            print("Automatic redial")
        elif callS == 2:
            print("Speed Dialling")
        elif callS == 3:
            print("Call Waiting Option")
        elif callS == 4:
            print("Own number Sending")
        elif callS == 5:
            print("Phone Line In Use")
        elif callS == 6:
            print("Automatic answer")
    elif setting == 2:
        print("""
        1 -> Language
        2 -> Cell info display
        3 -> Welcome note 
        4 -> Network Selection
        5 -> Light
        6 -> Confirms Sim service action
        """)
        phoneS = int(input("Enter your response: "))
        if phoneS == 1:
            print("Language")
        elif phoneS == 2:
            print("Cell info display: ")
        elif phoneS == 3:
            print("Welcome note")
        elif phoneS == 4:
            print("Network selection")
        elif phoneS == 5:
            print("Lights")
        elif phoneS == 6:
            print("Confirms Sim service action")
    elif setting == 3:
        print("""
            1 -> PIN code request
            2 -> Calling barrier service
            3 -> fixed dialling
            4 -> Closed user group
            5 -> Phone security
            6 -> Change access code 
            """)
        phoneS = int(input("Enter the response: "))
        if phoneS == 1:
            print("One")
        elif phoneS == 2:
            print("Calling barrier service")
        elif phoneS == 3:
            print("Fixed dialling")
        elif phoneS == 4:
            print("Closed user gropup")
        elif phoneS == 5:
            print("Phone security")
        elif phoneS == 6:
            print("Change access code: ")
    elif setting == 4:
        print("Restore Factory setting")
