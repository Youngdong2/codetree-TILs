def temp(n):
    if n==0:
        return

    print(n, end=' ')
    temp(n-1)
    print(n, end=' ')

n = int(input())
temp(n)