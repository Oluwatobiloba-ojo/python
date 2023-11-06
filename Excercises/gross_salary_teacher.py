def your_salary(name, periods):
    result = 0
    if periods <= 100:
        result = 20 * periods
    else:
        overt_time = periods - 100
        result = (25 * overt_time) + (20 * 100)
    return [name, periods, result]


name_of_teacher = input("Enter the name of the teacher:")
period = int(input("Enter the number of period used: "))
results = your_salary(name_of_teacher, period)
print(f"""
    Teacher Name: {results[0]}
    Periods: {results[1]}
    Gross pay: {results[2]}
    """)
