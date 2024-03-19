class Temp:
    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma

n = int(input())
arr = []
for i in range(n):
    name, ko, en, ma = input().split()
    temp = Temp(name, int(ko), int(en), int(ma))
    arr.append(temp)

arr = sorted(arr, key=lambda x: (-x.ko, -x.en, -x.ma))

for i in range(n):
    print(arr[i].name, arr[i].ko, arr[i].en, arr[i].ma)