def temp(m, A):
    answer = 0
    while m >= 1:
        if m%2!=0:
            answer+=A[m-1]
            m -= 1
        else:
            answer+=A[m-1]
            m = int(m/2)

    print(answer)

n, m = map(int, input().split())
A = list(map(int, input().split()))

temp(m, A)