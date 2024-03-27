class Temp:
    def __init__(self, h, w, index):
        self.h = h
        self.w = w
        self.index = index

n = int(input())

arr = []
for i in range(n):
    h, w = map(int, input().split())
    arr.append(Temp(h, w, i+1))

arr = sorted(arr, key=lambda x: (x.h, -x.w))

for i in range(n):
    print(arr[i].h, arr[i].w, arr[i].index)