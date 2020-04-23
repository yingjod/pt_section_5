import math


def nedge(n, g):
    """

    count it
    
    """

    area = n * (g ** 2) / (4 * math.tan(math.pi / n))

    print(f"area = {area:.2f}")


def main():
    """
    
    get number from user

    """

    n = eval(input())

    g = eval(input())
    nedge(n, g)


main()
