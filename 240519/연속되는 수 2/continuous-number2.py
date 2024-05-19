n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = []
count = 1
for i in range(n-1):
    if arr[i+1]==arr[i]:
        count+=1
    else:
        count=1
    answer.append(count)

print(max(answer))