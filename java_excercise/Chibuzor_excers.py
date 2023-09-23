number_one = 1
number_two = 2
number_three = 3
number_four = 4
number_five = 5
result = 1
result2 = 1
result3 = 1
result4 = 1
result5 = 1
#print("\ta\tb\tpower(a,b)")
for b in range(2, 3, 1):
    result = number_one ** b
    print(f"{number_one:>4} {b:>4} {result:>4}")
for b in range(3,4,1):
    result2 = number_two ** b
    print(f"{number_two:>4} {b:>4} {result2:>4}")
for b in range(4,5,1):
    result3 = number_three ** b
    print(f"{number_three:>4} {b:>4} {result3:>4}")
for b in range(5,6,1):
    result4 = number_four ** b
    print(f"{number_four:>4} {b:>4} {result4:>6}")
for b in range(6,7,1):
    result5 = number_five ** b
    print(f"{number_five:>4} {b:>4} {result5:>6}")


