class Temp:
    def __init__(self, name, num, loc):
        self.name = name
        self.num = num
        self.loc = loc

n = int(input())

arr=[]
for i in range(n):
    name, num, loc = input().split()
    temp = Temp(name, num, loc)
    arr.append(temp)

arr = sorted(arr, key=lambda x: x.name)

print(f"name {arr[-1].name}")
print(f"addr {arr[-1].num}")
print(f"city {arr[-1].loc}")