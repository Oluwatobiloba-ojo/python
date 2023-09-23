quarter = 25
dimes = 10
nickel = 5
pennies = 1
quarterNumber = 0
dimeNumber = 0
nickelNumber = 0
penniesNumber = 0
item = 1000
cent = 0.00
print(f"The cost of this goods is ${item}")
amount = int(input("Enter the amount you are to pay: "))
if amount <= item:
    print(f"The cost of ths goods is {item}")
    amount = int(input("Enter the amount you are to pay: "))
else:
    change = amount - item
    cent = change / 100
while cent != 0:
    if cent >= quarter:
        cent -= quarter
        quarterNumber += 1
    elif cent >= dimes:
        cent -= dimes
        dimeNumber += 1
    elif cent >= nickel:
        cent -= nickel
        nickelNumber += 1
    else:
        cent -= pennies
        penniesNumber += 1
print(f"""
    ===================================
    The changes is
    {quarterNumber} Quarter
    {dimeNumber} Dime
    {nickelNumber} Nickel
    {penniesNumber} Pennies
    ====================================
    """)
