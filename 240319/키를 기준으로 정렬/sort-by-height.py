class Temp:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

n = int(input())
arr = []
for i in range(n):
    name, tall, weight = input().split()
    temp = Temp(name, tall, weight)
    arr.append(temp)


arr = sorted(arr, key=lambda x: x.tall)

for i in range(n):
    print(f"{arr[i].name} {arr[i].tall} {arr[i].weight}")