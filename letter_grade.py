def letter_grade(score):
    try:
        score = float(score)
        if score > 1 or score < 0:
            raise Exception
    except:
        print("Enter a decimal number between 0 and 1 inclusive")

    if score >= 0.9:
        letter_grade = 'A'
    elif score >= 0.8:
        letter_grade = 'B'
    elif score >= 0.7:
        letter_grade = 'C'
    elif score >= 0.6:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade
