def make_rhombus(i, j, k, arr, n):
    count = 0
    # 맨해튼 거리 조건: |dx| + |dy| ≤ k
    for dx in range(-k, k+1):
        limit = k - abs(dx)
        for dy in range(-limit, limit+1):
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n:
                count += arr[x][y]
    return count

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):  # k는 0부터 시작 가능
            # 금 개수
            gold = make_rhombus(i, j, k, arr, n)
            # 비용 계산: K*K + (K+1)*(K+1)
            cost = k*k + (k+1)*(k+1)
            profit = gold * m - cost
            # 이익이 음수가 아니라면 최댓값 갱신
            if profit >= 0:
                answer = max(answer, gold)

print(answer)
