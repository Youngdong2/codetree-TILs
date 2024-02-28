def sub_seq(A, B):
    if len(A) >= len(B):
        for i in range(len(A)-len(B)+1):
            if A[i:i+len(B)]==B:
                return True
        return False

    else:
        for i in range(len(B)-len(A)+1):
            if B[i:i+len(A)]==A:
                return True
        return False


n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sub_seq(A, B):
    print('Yes')
else:
    print('No')