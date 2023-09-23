def investment_calculator(amount_to_invest, year, investment_rate):
    Starting_year = 1
    while Starting_year <= year:
        profit = amount_to_invest
        profit *= investment_rate / 100
        amount_to_invest += profit
        print(f"The ROI of this is {profit:.2f} at year{Starting_year} and accumulated money return is "
              f"{amount_to_invest:.2f}")
        Starting_year += 1


investment_calculator(10000, 25, 10)