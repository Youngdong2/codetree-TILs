n = int(input())

digit = []
while True:
    if n < 2:
        digit.append(n)
        break

    digit.append(n%2)
    n = n//2

digit = digit[::-1]

print(''.join([str(i) for i in digit]))