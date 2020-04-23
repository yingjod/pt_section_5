def compute(a, b, c):
    """

    count it

    """
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        res1 = (-b + delta ** 0.5) / (2 * a)
        res2 = (-b - delta ** 0.5) / (2 * a)
        return str(res1) + "," + str(res2)


def result_():
    """
    
    check the answer is no root or not
    
    """
    if result == None:
        print("your equation has no root")
    else:
        print(result)


if __name__ == "__main__":

    a = eval(input())
    b = eval(input())
    c = eval(input())
    result = compute(a, b, c)
    result()
