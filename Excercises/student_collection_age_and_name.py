def student_age(name: str, age=0):
    name = name.lower()
    result = 0
    student_list = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
    for student in student_list.keys():
        if student == name:
            result = student_list[student]
    if result == 0:
        result = age
        student_list[name] = age
    return result
