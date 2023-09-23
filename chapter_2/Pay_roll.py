name = input("Enter Employers name: ")
hour = float(input("Enter hours take in a week: "))
hour_rate = float(input("Enter hourly pay rate: "))
month = input("Enter the month:  ")
federal_rate = float(input("Enter the federal tax withholding rate:"))
state_rate = float(input("Enter the state tax withholding rate: "))

gross_pay = hour * hour_rate
federal_amount = federal_rate * gross_pay // 100
state_amount = state_rate * gross_pay // 100
Total_Deduction = federal_rate + state_rate
net_pay = gross_pay - Total_Deduction

print(f""""

    Employer name is: {name}
    Hours worked is: {hour}
    Pay rate is : {hour_rate}
    Gross pay is : {gross_pay}
    DEDUCTION :
    Federal withholding({federal_rate}): {federal_amount}
    State witholding ({state_rate}): {state_amount}
    Total deduction: {Total_Deduction}
    Net pay :{net_pay}

    """)
