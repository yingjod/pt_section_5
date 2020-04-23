def isLeap(year):
    """
    
    check is leap year or not

    """
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("%d is a leap year." % year)
    else:
        print("%d is not a leap year." % year)


def main():
    year = eval(input())
    isLeap(year)


main()
