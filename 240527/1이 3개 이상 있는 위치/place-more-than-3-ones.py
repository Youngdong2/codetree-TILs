n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

answer = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dir_num in range(4):
            nx, ny = i+ dx[dir_num], j + dy[dir_num]
            if 0<=nx and nx < n and 0<= ny and ny < n and arr[nx][ny]==1:
                count += 1

        if count >= 3:
            answer += 1

print(answer)