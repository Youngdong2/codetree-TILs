n = int(input())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

dir_dict = {"W": 0, "S": 1, "N": 2, "E": 3}

x, y = 0, 0

for _ in range(n):
    d, l = input().split()
    l = int(l)

    x = x + dx[dir_dict[d]]*l
    y = y + dy[dir_dict[d]]*l

print(x, y)