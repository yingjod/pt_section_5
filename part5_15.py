import math


def nedge(n, g):

    area = n * (g ** 2) / (4 * math.tan(math.pi / n))

    print(f"area = {area:.2f}")


def main():

    n = eval(input())

    g = eval(input())
    nedge(n, g)


main()
