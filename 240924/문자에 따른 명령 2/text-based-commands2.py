order = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = 3
x, y = 0, 0

for o in order:
    if o == "L":
        dir_num = (dir_num-1) % 4
    elif o == "R":
        dir_num = (dir_num+1) % 4
    elif o == "F":
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)