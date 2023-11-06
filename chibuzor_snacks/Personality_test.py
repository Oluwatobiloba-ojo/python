from chibuzor_snacks.personalInfo import displayPersonalType

questionA = [
    ["expend energy, enjoy group", "think out loud", "public activities", "express yourself", "active, initiate"],
    ["Interpret literally", "practical", "standard, usual", "focus on here and now", "Fact things, what it is"],
    ["logical, thinking", "candid, straight forward, frank", "Tough-minded, just", "issue oriented",
     "tend to criticize"],
    ["Organized, orderly", "plan, schedule", "regulated and structured", "Preparation, plan ahead", "control govern"],
]
numberA = 0
numberB = 0
personalType = ""
personalA = ["E", "S", "T", "J"]
personalB = ["I", "N", "F", "P"]
questionB = [["conserve energy, enjoy one on one", "think to yourself", "solitary activities", "keep to yourself",
              "reflective deliberate"],
             ["look for meaning and possibilities", "imaginative", "different, unique",
              "look to the future, global perspective,Big Picture", "dreams, what it could be"],
             ["empathetic, feeling", "tactful, kind,encouraging", "tender-hearted, merciful", "people oriented",
              "tend to appreciate"],
             ["flexible, adaptable", "unplanned, spontaneous", "easy going, live and let live",
              "go with the flow, adapt as you go", "latitude, freedom"],
             ]
totalAnswer = [["" for i in range(len(questionA[0]))] for col in range(len(questionA))]
# print(totalAnswer)
for value, num in enumerate(questionA):
    for idx, nums in enumerate(num):
        answer = input("A." + questionA[value][idx] + "\t" + "B." + questionB[value][idx] + "\n")
        answer = answer.upper()
        while answer != "A" and answer != "B":
            answer = input(questionA[value][idx] + "\t\t" + questionB[value][idx] + '\n').upper()
        if answer == "A":
            totalAnswer[value][idx] += answer + questionA[value][idx]
        elif answer == "B":
            totalAnswer[value][idx] += answer + questionB[value][idx]

for indices, ans in enumerate(totalAnswer):
    for count, _ in enumerate(ans):
        request = totalAnswer[indices][count]
        print(request)
        if request[0] == "A":
            numberA += 1
        else:
            numberB += 1
    if numberA > numberB:
        personalType += personalA[indices]
    else:
        personalType += personalB[indices]
    print("Number of A is ", numberA)
    print("Number of B is ", numberB)
    print()
    numberA = 0
    numberB = 0
displayPersonalType(personalType)