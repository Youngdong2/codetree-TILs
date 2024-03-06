def temp(A, a1, a2):
    s = 0
    for i in range(a1-1, a2):
        s += A[i]

    return s

n, m = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(temp(A, a1, a2))