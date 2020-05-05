def levelcheck(score, gpa):
    if 90 <= score and score <= 100:
        gpa = "A"
    elif 80 <= score and score <= 89:
        gpa = "B"
    elif 70 <= score and score <= 79:
        gpa = "C"
    elif 60 <= score and score <= 69:
        gpa = "D"
    else:
        gpa = "E"
    print("Your gpa is %s" % gpa)


if __name__ == "__main__":
    score = eval(input())
    gpa = 0
    levelcheck(score, gpa)
