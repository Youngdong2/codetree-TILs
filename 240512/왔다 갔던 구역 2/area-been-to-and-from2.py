n = int(input())

# 좌표 범위를 설정합니다.
arr = [0]*2000
offset = 1000
state = offset

for i in range(n):
    x, direction = input().split()
    x = int(x)
    
    # 오른쪽으로 이동하는 경우
    if direction == 'R':
        for j in range(state, state + x):
            arr[j] += 1
        state += x  # 상태 업데이트

    # 왼쪽으로 이동하는 경우
    else:
        for j in range(state - x, state):
            arr[j] += 1
        state -= x  # 상태 업데이트

count = 0
# 2번 이상 방문한 위치를 세는 로직
for a in arr:
    if a >= 2:
        count += 1

print(count)