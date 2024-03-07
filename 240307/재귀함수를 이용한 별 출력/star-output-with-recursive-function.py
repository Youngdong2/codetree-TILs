def temp(n):
    if n==0:
        return

    temp(n-1)
    print('*'*n)

n = int(input())

temp(n)