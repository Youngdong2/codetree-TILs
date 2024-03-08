def temp(n):
    if n==1:
        return 1

    return temp(n-1) + n

n = int(input())
print(temp(n))