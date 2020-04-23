import random
def randnum(num):
    for i in range(1,num+1):
        rn=random.randint(1,100)
        if i % 10 == 0:
            print('%4d'%rn)
        else:
            print('%4d'%(rn),end=' ')


def main():
    num=eval(input())
    randnum(num)

main()