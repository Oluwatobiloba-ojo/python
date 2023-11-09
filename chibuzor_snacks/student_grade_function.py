def total_of_scores(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def display_subject(subject):
    print("===============================================")
    print("Student ", end="\t")
    for i in range(subject):
        print(f"SUB{i + 1} ", end="\t")
    print("TOT\t\t", "AVE\t\t", "POS")


def position(numbers):
    positions = [1 for i in range(len(numbers))]
    for index in range(len(numbers)):
        for idx in range(len(numbers)):
            if numbers[index] < numbers[idx]:
                positions[index] += 1
    return positions


def highest_scoring_student(numbers):
    maximum = numbers[0]
    student = 1
    for idx, value in enumerate(numbers):
        if value > maximum:
            maximum = value
            student = idx + 1
    return student


def highest_score(numbers):
    return max([grade for grade in numbers])


def lower_score(numbers):
    return min([i for i in numbers])


def lower_student_score(numbers):
    minimum = numbers[0]
    student = 1
    for idx, value in enumerate(numbers):
        if value < minimum:
            minimum = value
            student = idx + 1
    return student


def number_of_passes(grades):
    lists = [i for i in grades if i > 50]
    return len(lists)


def number_of_failure(grades):
    lists_of_grades = [grade for grade in grades if grade < 50]
    return len(lists_of_grades)


def checks_the_greatest_numbers_of_pass(grades):
    numbers = grades[0]
    for value in grades:
        if value > numbers:
            numbers = value
    return numbers


def checks_the_greatest_subject_pass(grades):
    numbers = grades[0]
    subject = 0
    for index, value in enumerate(grades):
        if value > numbers:
            numbers = value
            subject = index
    return subject


def check_for_the_greatest_score_in_a_2D_list(grades):
    maximum = grades[0][0]
    for scores in grades:
        for score in scores:
            if score > maximum:
                maximum = score
    return maximum


def check_for_the_greatest_student(grades):
    maximum = grades[0][0]
    student = 0
    for scores in grades:
        for index, score in enumerate(scores):
            if score > maximum:
                maximum = score
                student = index + 1
    return student


def check_for_the_lowest_score_in_a_2D_list(grades):
    minimum = grades[0][1]
    for scores in grades:
        for score in scores:
            if score < minimum:
                minimum = score
    return minimum


def check_for_the_subject_with_highest_score(grades, sub):
    subject = 1
    maximum = grades[0][0]
    student = 1
    for value in range(sub):
        for idx, stud in enumerate(grades):
            if grades[idx][value] > maximum:
                maximum = grades[idx][value]
                student = idx + 1
                subject = value + 1
    return [subject, student, maximum]


def check_for_the_lowest(grades, numberOfSubject):
    student = 1
    subject = 1
    minimum = grades[0][0]
    for value in range(numberOfSubject):
        for idx, score in enumerate(grades):
            if grades[idx][value] < minimum:
                minimum = grades[idx][value]
                student = idx + 1
                subject = value + 1
    return [subject, student, minimum]


def check_for_the_overall_highest_score(grades):
    student = 0
    maximum = grades[0]
    for idx, value in enumerate(grades):
        if value > maximum:
            maximum = value
            student = idx + 1
    return [student, maximum]


def check_for_the_overall_lowest_score(grades):
    student = 1
    minimum = grades[0]
    for index, value in enumerate(grades):
        if value < minimum:
            minimum = value
            student = index + 1
    return [student, minimum]


def display_subject_summary(subject, student, student_lists):
    lists_of_subject_passes = [1 for passes in range(subject)]
    lists_of_subject_failure = [1 for failure in range(subject)]
    for value in range(subject):
        numbers = [0 for i in range(student)]
        for idx in range(student):
            numbers[idx] = student_lists[idx][value]
        lists_of_subject_passes[value] = number_of_passes(numbers)
        lists_of_subject_failure[value] = number_of_failure(numbers)
        print(f"""
        SUBJECT {value + 1}
        The Highest Scoring is: Student {highest_scoring_student(numbers)} scoring {highest_score(numbers)}
        The lowest Scoring is: Student {lower_student_score(numbers)} scoring {lower_score(numbers)}
        The total score is: {total_of_scores(numbers)}
        The average score is: {total_of_scores(numbers) / len(numbers):.2f}
        Number of passes:   {number_of_passes(numbers)}
        Number of failures: {number_of_failure(numbers)}
        """)
    return [lists_of_subject_passes, lists_of_subject_failure]


def class_summary(student_lists, lists_of_subject_failure, lists_of_subject_passes, subject, totalTotal):
    hardest_subject = checks_the_greatest_subject_pass(lists_of_subject_failure) + 1
    hardest_subject_score = checks_the_greatest_numbers_of_pass(lists_of_subject_failure)
    easiest_subject = checks_the_greatest_subject_pass(lists_of_subject_passes) + 1
    easiest_subject_score = checks_the_greatest_numbers_of_pass(lists_of_subject_passes)
    highest_subject_score = check_for_the_subject_with_highest_score(student_lists, subject)
    overall_lowest_score = check_for_the_lowest(student_lists, subject)
    total_sum = total_of_scores(totalTotal)
    highest_total_of_scores = check_for_the_overall_highest_score(totalTotal)
    lowest_total_of_scores = check_for_the_overall_lowest_score(totalTotal)
    return [hardest_subject, hardest_subject_score, easiest_subject, easiest_subject_score, highest_subject_score[0],
            highest_subject_score[1], highest_subject_score[2], overall_lowest_score[0], overall_lowest_score[1],
            overall_lowest_score[2], highest_total_of_scores[0], highest_total_of_scores[1], lowest_total_of_scores[0],
            lowest_total_of_scores[1], total_sum]


def display_class_summary(class_summarys, totalTotal):
    print(f"""
    The hardest subject is Subject {class_summarys[0]} with {class_summarys[1]} failure
    The easiest subject is Subject {class_summarys[2]} with {class_summarys[3]} passes
    The overall highest score is Student {class_summarys[5]} Subject {class_summarys[4]} with score {class_summarys[6]}
    The overall lowest score is Student {class_summarys[8]} Subject {class_summarys[7]} with score {class_summarys[9]}
    =====================================================================

    CLASS SUMMARY
    =====================================================================
    BEST GRADUATING STUDENT IS: STUDENT {class_summarys[10]} SCORING {class_summarys[11]}
    =====================================================================

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    WORST GRADUATING STUDENT IS: STUDENT {class_summarys[12]} SCORING {class_summarys[13]}
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ======================================================================
    CLASS TOTAL: {class_summarys[14]}
    CLASS AVERAGE: {class_summarys[14] / len(totalTotal):.2f}
    ======================================================================
        """)
