def temp(n):
    if n==1:
        return 1
    if n==2:
        return 2

    return temp(n//3) + temp(n-1)

n = int(input())

print(temp(n))