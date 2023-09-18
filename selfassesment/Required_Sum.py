addition = 0
Begin_Value = int(input("Enter a number: "))
while addition < Begin_Value:
    value = int(input("Enter a number: "))
    addition += value

print(f"""
                The first userInput is {Begin_Value}
                The sum of this value collected is {addition}
    """)