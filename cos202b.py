name = input("Input your name: ")

try:
    score_input = input("Input your score: ")
    score = int(score_input)

    if score <= 10:
        grade = "F (Fail)"
    elif score <= 25:
        grade = "D (Fair)"
    elif score <= 40:
        grade = "E (Pass)"
    elif score <= 50:
        grade = "C (Good)"
    elif score <= 69:
        grade = "B (Very Good)"
    elif score <= 100:
        grade = "A (Excellent)"
    else:
        grade = "Score out of range"

    print(f"{name}, your grade is: {grade}")
    
except:
    print("Invalid Score")
