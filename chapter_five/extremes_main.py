from extremes import extremes

number_of_times = int(input("Enter the number of times: "))
lists = []
for number in range(number_of_times):
    num = int(input("Enter the number: "))
    lists.append(num)
print(extremes(lists))
