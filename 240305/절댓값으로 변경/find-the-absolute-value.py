def temp(li):
    print(' '.join([str(abs(s)) for s in li]))

n = int(input())
li = list(map(int, input().split()))
temp(li)