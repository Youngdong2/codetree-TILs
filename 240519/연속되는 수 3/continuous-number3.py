n = int(input())
arr = []
for _ in range(n):
    m = input()
    if len(m)==1:
        arr.append('+')
    else:
        arr.append(m[0])

answer = []
count = 1
for i in range(n-1):
    if arr[i+1]==arr[i]:
        count += 1
    else:
        answer.append(count)
        count = 1

answer.append(count)
print(max(answer))