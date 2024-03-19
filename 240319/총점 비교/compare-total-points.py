class Temp:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

n = int(input())

arr = []
for i in range(n):
    name, s1, s2, s3 = input().split()
    temp = Temp(name, int(s1), int(s2), int(s3))
    arr.append(temp)

arr = sorted(arr, key=lambda x: x.s1 + x.s2 + x.s3)

for i in range(n):
    print(arr[i].name, arr[i].s1, arr[i].s2, arr[i].s3)