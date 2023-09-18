numbers = int(input("Enter a number: "))
value = 1
product = 1.0
add = 1.0
index = 1
while index <= numbers:
    add = add * (1.0 / index)
    product += add
    index += 1
print(product)
