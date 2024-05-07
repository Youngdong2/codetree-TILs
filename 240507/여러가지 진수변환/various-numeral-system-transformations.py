n, b = map(int, input().split())

answer = []
while True:
    if n < b:
        answer.append(n)
        break

    answer.append(n%b)
    n = n//b

for digit in answer[::-1]:
    print(digit, end="")