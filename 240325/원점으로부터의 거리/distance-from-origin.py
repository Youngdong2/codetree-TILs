n = int(input())

class Temp:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((Temp(x, y), i+1))

arr = sorted(arr, key=lambda x: (abs(x[0].x)+abs(x[0].y), i))

for i in range(n):
    print(arr[i][1])