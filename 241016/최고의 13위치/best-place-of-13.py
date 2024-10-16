n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(n-2):
        count = max(count, arr[i][j]+arr[i][j+1]+arr[i][j+2])

print(count)