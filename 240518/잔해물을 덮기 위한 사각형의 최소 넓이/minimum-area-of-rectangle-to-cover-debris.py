# 입력받기
rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))

# 범위 설정
OFFSET = 1000
SIZE = 2001

# 배열 초기화
arr = [[0] * SIZE for _ in range(SIZE)]

# 첫 번째 직사각형 표시
for i in range(rect1[0] + OFFSET, rect1[2] + OFFSET):
    for j in range(rect1[1] + OFFSET, rect1[3] + OFFSET):
        arr[i][j] = 1

# 두 번째 직사각형으로 덮기
for i in range(rect2[0] + OFFSET, rect2[2] + OFFSET):
    for j in range(rect2[1] + OFFSET, rect2[3] + OFFSET):
        arr[i][j] = 0

# 남아있는 첫 번째 직사각형 영역 찾기
min_x, max_x = SIZE, -1
min_y, max_y = SIZE, -1

for i in range(SIZE):
    for j in range(SIZE):
        if arr[i][j] == 1:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j

# 남아있는 영역이 없으면 넓이는 0
if min_x == SIZE:
    print(0)
else:
    # 최소 직사각형의 넓이 계산
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    area = width * height
    print(area)