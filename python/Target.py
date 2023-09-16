age = int(input("Enter your age: "))

maximum_Heart_rate = 220 - age

begin = float(50 / 100) * maximum_Heart_rate
end = float(85 / 100) * maximum_Heart_rate

print("target heart rate is from", begin, "and", end)