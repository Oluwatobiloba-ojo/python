def student_age(name: str):
    name = name.lower()
    result = 0
    student_list = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
    for student in student_list.keys():
        if student == name:
            result = student_list[student]
    if result == 0:
        result = int(input("Your name is not in the database you can try and add your age: "))
        student_list[name] = result
        print(student_list)
    return result


names = input("Enter your name ")
print("Hi ", names, " is ", student_age(names), " years old ")
