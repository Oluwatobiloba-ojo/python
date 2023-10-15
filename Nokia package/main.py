from Message import function_message
from Nokia_function import Tones, Setting
from call_register import CallRegister, Clock
from phoneBook import phoneBook
from Calculator import Calculator


response = int(input("""
    1 -> PhoneBook
    2 -> Message
    3 -> Chat
    4 -> Call Register
    5 -> Tones
    6 -> Setting
    7 -> Call divert
    8 -> Games
    9 -> Calculator
    10 -> Reminder
    11 -> Clock
    12 -> Profiles
    13 -> Sim Service
    """))
if response == 1:
    phoneBook()
elif response == 2:
    function_message()
elif response == 3:
    print("Chat")
elif response == 4:
    CallRegister()
elif response == 5:
    Tones()
elif response == 6:
    Setting()
elif response == 7:
    print("Call Divert")
elif response == 8:
    print("Games")
elif response == 9:
    Calculator()
elif response == 10:
    print("Reminder")
elif response == 11:
    Clock()
elif response == 12:
    print("Profiles")
elif response == 13:
    print("Sim service")