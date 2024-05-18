arr = [[0]*2000 for _ in range(2000)]

for k in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if k==0:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
min_x, max_x = 2000, -1
min_y, max_y = 2000, -1

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j

width = max_x - min_x + 1
height = max_y - min_y + 1
area = width * height
print(area)