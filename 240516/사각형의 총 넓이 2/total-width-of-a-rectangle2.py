n = int(input())

arr = [[0]*200 for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

print(sum(sum(row) for row in arr))