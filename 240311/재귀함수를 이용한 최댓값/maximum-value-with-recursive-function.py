n = int(input())
A = list(map(int, input().split()))

def temp(n):
    if n==0:
        return A[0]

    return max(temp(n-1), A[n])


print(temp(n-1))