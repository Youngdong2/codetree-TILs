n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = []
count = 1
for i in range(n - 1):
    if (arr[i] > 0 and arr[i + 1] > 0) or (arr[i] < 0 and arr[i + 1] < 0):
        count += 1
    else:
        answer.append(count)
        count = 1

answer.append(count)
print(max(answer))