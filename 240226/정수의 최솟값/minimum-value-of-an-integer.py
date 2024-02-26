def func(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input().split())

print(func(a, b, c))