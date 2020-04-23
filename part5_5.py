def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(a, end=" ")
        print()


if __name__ == "__main__":

    a = input()
    x = int(input())
    y = int(input())
    compute(a, x, y)
