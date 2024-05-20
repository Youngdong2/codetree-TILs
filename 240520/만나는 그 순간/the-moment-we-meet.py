n, m = map(int, input().split())

# A와 B의 위치를 기록할 리스트
positions_a = []
positions_b = []

# 현재 위치 초기화
current_position_a = 0
current_position_b = 0

# A의 움직임 기록
for _ in range(n):
    direction, l = input().split()
    l = int(l)
    for _ in range(l):
        if direction == 'R':
            current_position_a += 1
        else:
            current_position_a -= 1
        positions_a.append(current_position_a)

# B의 움직임 기록
for _ in range(m):
    direction, l = input().split()
    l = int(l)
    for _ in range(l):
        if direction == 'R':
            current_position_b += 1
        else:
            current_position_b -= 1
        positions_b.append(current_position_b)

# 두 리스트의 길이가 같아야 함을 가정
assert len(positions_a) == len(positions_b)

# 두 리스트를 비교하여 최초로 같은 위치에 있는 시간 찾기
meeting_time = -1
for t in range(len(positions_a)):
    if positions_a[t] == positions_b[t]:
        meeting_time = t + 1  # t가 0부터 시작하므로 +1
        break

print(meeting_time)