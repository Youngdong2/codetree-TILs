def temp(a, b):
    if a <= b:
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10

    return a, b

a, b = map(int, input().split())
a, b = temp(a, b)
print(f"{a} {b}")