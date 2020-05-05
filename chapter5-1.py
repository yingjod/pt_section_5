def multiply99():

    for i in range(1, 10):
        for j in range(1, 10):
            print("%d * %d= %2d" % (j, i, j * i), end="  ")

        print()


def printstar():
    for i in range(1, 73):
        print("*", end="")
    print()


if __name__ == "__main__":
    printstar()
    multiply99()
    printstar()
