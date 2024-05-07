a, b = map(int, input().split())
n = int(input())

num = 0
for i in range(len(str(n))):
    num = num * a + int(str(n)[i])

answer = []
while True:
    if num < b:
        answer.append(num)
        break

    answer.append(num%b)
    num = num//b

print(''.join([str(i) for i in answer[::-1]]))