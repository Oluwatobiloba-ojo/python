passes = 0
failure = 0
for number in range (10):
	num = int(input("Enter a number, 1 = passes, 2 = failes"))
	if num == 1:
		passes = passes + 1
	else: 
		failure = failure + 1
print("Passes is ", passes)
print("failure is ", failure)

if passes >= 8:
	print("Bonus to instructor") 