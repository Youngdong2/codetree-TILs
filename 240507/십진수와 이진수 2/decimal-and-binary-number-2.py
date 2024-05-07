n = int(input())

num = 0
for i in range(len(str(n))):
    num = num * 2 + int(str(n)[i])

m = num * 17

answer = []
while True:
    if m < 2:
        answer.append(m)
        break

    answer.append(m%2)
    m = m//2

for digit in answer[::-1]:
    print(digit, end="")