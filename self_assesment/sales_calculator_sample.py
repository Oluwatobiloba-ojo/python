def calculate_gross_pay(*amount):
    total = 0
    for value in amount:
        total += value
    result1 = 0.09 * total
    result = result1 + 200
    return f"{result:.2f}"


print(calculate_gross_pay(230, 350, 120.0, 450))