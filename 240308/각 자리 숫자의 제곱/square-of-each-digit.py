def temp(n):
    if n < 10:
        return n**2

    return temp(n//10) + (n%10)**2


n = int(input())
print(temp(n))