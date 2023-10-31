def first_question():
    question = """
    1. Which of the following is a green house gas
    that is released by human activities and 
    speed up global warming
    a. Petroleum        c. Carbon Dioxide
    b. Natural gas      d. nuclear power"""
    return question


def second_question():
    question = """
    2. Which of the following human activities
    does not release carbon dioxide into the
    atmosphere
    a. Burning fossil fuel     b. Deforestation
    c. Fishing                  d. Driving"""
    return question


def third_question():
    question = """
    3. Rising water temperature is a result of global
    warming and may eventually increase sea levels
    due to dissolving of what
    a. mountains                     b. wetlands
    c. river beds                    d. glaciers"""
    return question


def fourth_question():
    question = """
    4. As global warming continues the intensity of
    of what types of storm that hits coastline
    is predicted to increase
    a. tornadoes                c. hurricanes
    b. tsunamis                 d. earthQuakes"""
    return question


def fifth_question():
    question = """
        5. Which of the following is not a negative
        effect of global warming
        a. Larger fish population        c. species extinction
        b. new infectious diseases       d. less of coastal areas"""
    return question


def display_and_get_input():
    count = 0
    answer = input(first_question()+ "\n").lower()
    if answer == 'c': count += 1
    answer = input(second_question()+ "\n").lower()
    if answer == 'c': count += 1
    answer = input(third_question() + "\n").lower()
    if answer == "d": count += 1
    answer = input(fourth_question()+ "\n").lower()
    if answer == 'c': count += 1
    answer = input(fifth_question()+ "\n").lower()
    if answer == 'a': count += 1
    return count


def response(test_marked):
    result = ''
    if test_marked == 5:
        result = 'Excellent'
    elif test_marked == 4:
        result = 'Very Good'
    else:
        result = 'Time to brush up on your knowledge of global warming\
                 GLOBAL WARMING ON EARTH' \
                 'GLOBAL WARMING 101' \
                 'CLIMATE CHANGE'
    return result
