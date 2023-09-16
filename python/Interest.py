principal = int(input("Enter the value of the amount invested: "))
rate = int(input("Enter the annual rate: "))
ten_years = 10 
twenty_years = 20
thirthy_years = 30

convert_rate = rate / 100
answer = principal * (1 + convert_rate) ** ten_years
answer_twenty = principal * (1 + convert_rate) ** twenty_years
answer_thirthy = principal * (1 + convert_rate) ** thirthy_years


print("Amount on deposit at the end of the ten year given is",  answer)
print("Amount on deposit at the end of the twenty year given is",  answer_twenty)
print("Amount on deposit at the end of the thirthy year given is",  answer_thirthy)