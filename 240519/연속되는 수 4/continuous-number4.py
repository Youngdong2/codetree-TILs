n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = []
count = 0
for i in range(n-1):
    if arr[i]<arr[i+1]:
        count += 1
    else:
        answer.append(count)
        count = 1

answer.append(count)
print(max(answer))