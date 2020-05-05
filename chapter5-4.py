def totalandmean():
    sum = 0
    for i in range(1, 11):
        num = eval(input())
        sum += num
    average = sum / 10
    return sum, average


if __name__ == "__main__":
    sum, average = totalandmean()
    print("sum=%.2f , mean=%.2f" % (sum, average))
