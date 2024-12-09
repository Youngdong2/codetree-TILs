n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

for i in range(n):
    for j in range(m):
        if j+2 < m:
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if s > answer:
                answer = s

        if i+2 < n:
            s = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if s > answer:
                answer = s

        if i+1 < n and j+1 < m:
            s = arr[i][j] + arr[i][j+1] + arr[i+1][j]
            if s > answer:
                answer = s

        if i+1 < n and j+1 < m:
            s = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
            if s > answer:
                answer = s

        if i + 1 < n and j + 1 < m:
            s = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
            if s > answer:
                answer = s

        if i + 1 < n and j + 1 < m:
            s = arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
            if s > answer:
                answer = s

print(answer)
        