def compute(n):

    """
    to count the number
    """
    n1 = 0
    n2 = 1
    print("%d %d" % (n1, n2), end=" ")
    for i in range(3, n + 1):
        n3 = n1 + n2
        print("%d" % (n3), end=" ")
        n1 = n2
        n2 = n3


if __name__ == "__main__":

    num = eval(input())
    compute(num)
