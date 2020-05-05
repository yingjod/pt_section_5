def LEVEL(hight, weight):
    BMI = weight / (hight / 100) ** 2
    answer = 0
    if BMI < 18.5:
        answer = " under weight"
    elif BMI < 25 and BMI >= 18.5:
        answer = "normal"
    elif BMI < 30 and BMI >= 25:
        answer = "over weight "
    else:
        answer = "fat"
    print("your bmi is %s" % answer)


if __name__ == "__main__":
    hight = eval(input())
    weight = eval(input())
    LEVEL(hight, weight)
