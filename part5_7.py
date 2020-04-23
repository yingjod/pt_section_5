import math


def compute(num):
    s_num = math.floor(num ** 0.5)
    for i in range(2, (s_num + 1)):
        if (num % i) == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input())
    if num > 1:
        if compute(num):
            print("prime")
        else:
            print("not prime")
    else:
        print("not prime")
