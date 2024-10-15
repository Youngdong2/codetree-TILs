n = int(input())

x, y = 0, 0

# 방향을 W, S, N, E로 매핑 (서, 남, 북, 동)
direction = {"W": 0, "S": 1, "N": 2, "E": 3}

# 각각 서, 남, 북, 동 이동을 나타냄
dx = [-1, 0, 0, 1]  # W, S, N, E
dy = [0, -1, 1, 0]  # W, S, N, E

times = 0
found = False  # 처음으로 (0, 0)에 도착했는지 여부를 저장할 변수

# N번의 이동에 대해 반복
for _ in range(n):
    d, l = input().split()  # 방향과 거리를 입력받음
    l = int(l)  # 이동 거리를 정수로 변환

    # 이동 거리를 한 칸씩 처리
    for _ in range(l):
        # 매초마다 한 칸씩 이동
        x += dx[direction[d]]
        y += dy[direction[d]]
        times += 1  # 1초 경과

        # (0, 0)에 도착했는지 확인
        if x == 0 and y == 0:
            found = True  # 도착했다는 표시
            break  # 더 이상 이동하지 않고 반복문 탈출

    if found:  # (0, 0)에 도착한 경우 더 이상 이동할 필요 없으므로 반복문 종료
        break

# (0, 0)에 도착했으면 걸린 시간을 출력, 그렇지 않으면 -1 출력
if found:
    print(times)
else:
    print(-1)