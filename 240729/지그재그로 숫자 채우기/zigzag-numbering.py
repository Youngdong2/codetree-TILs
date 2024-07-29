n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

num = 0
for col in range(m):
    if col%2 == 0:
        for row in range(n):
            arr[row][col] = num
            num += 1

    else:
        for row in range(n-1, -1, -1):
            arr[row][col] = num
            num += 1

for row in arr:
    print(' '.join(map(str, row)))