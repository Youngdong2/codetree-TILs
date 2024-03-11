def temp(n):
    if n < 10:
        return n

    return temp(n//10) + n%10


a, b, c = map(int, input().split())

print(temp(a*b*c))