def compute(x, y):
    gcd = 1
    k = 1
    if a > 0 and b > 0:
        while k <= a and k <= b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return gcd


if __name__ == "__main__":

    x, y = eval(input())
    gcd = compute(x, y)
    print(gcd)
