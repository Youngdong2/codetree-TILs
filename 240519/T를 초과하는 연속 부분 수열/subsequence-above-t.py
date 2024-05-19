n, t = map(int, input().split())

arr = list(map(int, input().split()))
answer = []
count = 1
for i in range(n-1):
    if arr[i+1]>t and arr[i]>t:
        count += 1
    else:
        answer.append(count)
        count = 1

answer.append(count)

print(max(answer))