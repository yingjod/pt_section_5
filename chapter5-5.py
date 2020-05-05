import math


def distance(x1, y1, x2, y2):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dis


def main():
    a, b = eval(input())
    c, d = eval(input())

    dd = distance(a, b, c, d)
    print("the distance of ((%d,%d),(%d,%d)=%.2f" % (a, b, c, d, dd))


main()
