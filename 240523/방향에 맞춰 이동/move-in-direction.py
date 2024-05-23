n = int(input())
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction_map = {"N":3, "E":0, "S":1, "W": 2}

for _ in range(n):
    direction, r = input().split()
    r = int(r)
    x = x + dx[direction_map[direction]]*r
    y = y + dy[direction_map[direction]]*r

print(x, y)