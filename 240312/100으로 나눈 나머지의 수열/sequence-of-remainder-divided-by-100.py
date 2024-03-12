def temp(n):
    if n==1:
        return 2
    if n==2:
        return 4

    return (temp(n-1) * temp(n-2)) % 100

n = int(input())
print(temp(n))