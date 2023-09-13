import random

generate_number = random.randint(1, 10)
user_number = int(input("Enter a number"))
if generate_number == user_number:
    print("You won congratulation")
elif generate_number != user_number:
    print("You lose !!!!!!!")

while generate_number != user_number:
    user_number = int(input("Enter a number: "))

    if user_number == generate_number:
        print("You won congratulation")

    elif user_number != generate_number:
        print("You lose !!!!!!!")
