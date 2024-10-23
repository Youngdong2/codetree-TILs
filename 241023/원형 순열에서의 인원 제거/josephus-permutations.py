from collections import deque

n, k = map(int, input().split())
answer = []

q = deque()
for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())

    answer.append(q.popleft())

print(*answer)