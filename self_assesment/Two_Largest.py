largest = 0
largest2 = 0
#for count in range(1,11):
 #   numbers = int(input("Enter a number: "))
#    if numbers > largest:
#        largest2 = largest
#        largest = numbers
#    elif largest2 < numbers:
#        largest2 = numbers
#print("The overall largest number is ", largest)
#print("The second largest number is ", largest2)


counter = 0
while counter < 10:
    numbers = int(input("Enter a number: "))
    if numbers > largest:
        largest2 = largest
        largest = numbers
    elif largest2 < numbers:
        largest2 = numbers
    counter += 1
print("The overall largest number is ", largest)
print("The second largest number is ", largest2)

