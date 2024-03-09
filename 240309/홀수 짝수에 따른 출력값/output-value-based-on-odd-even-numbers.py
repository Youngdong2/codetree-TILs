def temp(n):
    if n==1:
        return 1
    if n==2:
        return 2

    return temp(n-2)+n

n = int(input())
print(temp(n))