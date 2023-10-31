count_a, count_b, count_c, count_d = 0, 0, 0, 0
for num in range(5):
    name = input("Enter your name: ")
    grade = input("Enter your grade: ").upper()
    while grade not in ['A', 'B', 'C', 'D']:
        print("Invalid input")
        grade = input("Enter your grade: ").upper()
    if grade == 'A':
        count_a += 1
    elif grade == 'B':
        count_b += 1
    elif grade == 'C':
        count_c += 1
    elif grade == 'D':
        count_d += 1

print(f"""
Numbers of A: {count_a}
Numbers of B: {count_b}    
Numbers of C: {count_c}
Number of D: {count_d}
""")