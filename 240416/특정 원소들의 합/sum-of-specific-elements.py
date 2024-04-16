arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))

s = 0
for i in range(4):
    s += sum(arr[i][:i+1])

print(s)