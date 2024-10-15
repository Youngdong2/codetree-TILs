n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1  # 0-based index로 맞춤
c = int(c) - 1  # 0-based index로 맞춤

# 방향을 U, D, R, L로 매핑
dir_map = {"U": 0, "D": 1, "R": 2, "L": 3}

# 각각 상, 하, 우, 좌 이동을 나타냄
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 범위 내에 있는지 확인하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 방향 반전 함수
def reverse_direction(d):
    if d == "U":
        return "D"
    elif d == "D":
        return "U"
    elif d == "R":
        return "L"
    elif d == "L":
        return "R"

# 초기 위치
x, y = r, c

# t초 동안 반복
for _ in range(t):
    # 이동할 다음 위치 계산
    nx = x + dx[dir_map[d]]
    ny = y + dy[dir_map[d]]

    # 벽에 부딪히면 방향을 반대로 바꿔줌 (이동하지 않고 방향만 바꿈)
    if not in_range(nx, ny):
        d = reverse_direction(d)
    else:
        # 벽에 부딪히지 않으면 위치 업데이트
        x = nx
        y = ny

# 최종 위치 출력 (1-based index로 출력)
print(x + 1, y + 1)