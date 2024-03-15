n = int(input())
arr = list(map(int, input().split()))

answer = []
for i in range(n):
    if i%2==0:
        answer.append(arr[i//2])

print(*answer)