class Temp:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
arr = []
for i in range(n):
    name, h, w = input().split()
    arr.append(Temp(name, int(h), int(w)))

arr = sorted(arr, key=lambda x: (x.h, -x.w))

for i in range(n):
    print(arr[i].name, arr[i].h, arr[i].w)