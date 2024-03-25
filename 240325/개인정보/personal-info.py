class Temp:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

arr = []
for i in range(5):
    name, h, w = input().split()
    arr.append(Temp(name, h, w))

arr1 = sorted(arr, key=lambda x: x.name)
arr2 = sorted(arr, key=lambda x: x.h, reverse=True)

print('name')
for i in range(5):
    print(arr1[i].name, arr1[i].h, round(float(arr1[i].w), 1))

print()

print('height')
for i in range(5):
    print(arr2[i].name, arr2[i].h, round(float(arr2[i].w), 1))