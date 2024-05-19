n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

count = []
for i in range(n):
    if i==0 or arr[i]!=arr[i-1]:
        count.append(i)

answer = []
if len(count)>1:
    for i in range(1, len(count)):
        answer.append(count[i]-count[i-1])
else:
    answer.append(1)
print(max(answer))