# def compute(a,b):
#     sum=0
#     for i in range(a,b+1):
#         sum += i
#     return sum
#
#
#
# a=eval(input())
# b=eval(input())
# print(compute(a,b))


def compute(a, b):
    return int((a + b) * (b - a + 1) / 2)


if __name__ == "__main__":
    a = eval(input())
    b = eval(input())
    print(compute(a, b))
