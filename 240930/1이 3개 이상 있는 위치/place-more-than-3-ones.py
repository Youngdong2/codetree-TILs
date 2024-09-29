n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

nx = [0, -1, 0, 1]
ny = [1, 0, -1, 0]

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

answer = 0
for i in range(n):
    for j in range(n):
        cnt=0
        for dir_num in range(4):
            x = i + nx[dir_num]
            y = j + ny[dir_num]

            if is_range(x, y) and arr[x][y]==1:
                cnt += 1

        if cnt >= 3:
            answer += 1

print(answer)