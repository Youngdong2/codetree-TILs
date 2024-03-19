class Temp:
    def __init__(self, h, w, n=0):
        self.h = h
        self.w = w
        self.n = n

n = int(input())
arr = []
for i in range(n):
    h, w = map(int, input().split())
    temp = Temp(h, w, i+1)
    arr.append(temp)

arr = sorted(arr, key=lambda x: (-x.h, -x.w, x.n))

for t in arr:
    print(t.h, t.w, t.n)