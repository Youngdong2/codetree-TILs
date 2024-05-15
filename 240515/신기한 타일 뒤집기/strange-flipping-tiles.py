n = int(input())

# 타일 상태를 저장할 배열 (0은 회색, 1은 흰색, -1은 검은색)
arr = [0] * (2 * 1000 * 100)
offset = 1000 * 100

# 초기 위치
current_position = offset

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'R':
        for i in range(current_position, current_position + x):
            arr[i] = -1  # 오른쪽으로 뒤집어서 검은색으로 변경
        current_position += (x - 1)
    else:
        for i in range(current_position, current_position - x, -1):
            arr[i] = 1  # 왼쪽으로 뒤집어서 흰색으로 변경
        current_position -= (x - 1)

# 흰색 타일과 검은색 타일의 개수 세기
white_count = arr.count(1)
black_count = arr.count(-1)

print(white_count, black_count)