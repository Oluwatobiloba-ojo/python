principal = 1000
rate = (1 + (7 / 100))
for year in range(1, 31):
    investment = principal * rate ** year
    print(f"Year\tAmount invested ")
    print(f"{year:> 4} {investment:> 4}")
