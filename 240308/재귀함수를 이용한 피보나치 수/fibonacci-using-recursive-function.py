def temp(n):
    if n==1:
        return 1

    if n==2:
        return 1

    return temp(n-1)+temp(n-2)


n = int(input())

print(temp(n))