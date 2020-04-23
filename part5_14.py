def factor(n):
    for i in range (1,n+1):
        factor=1
        print('%d ! = '%i,end='')
        for j in range(1,i+1):
            factor*=j
        print(factor)

def main():
    n=eval(input())
    factor(n)

main()