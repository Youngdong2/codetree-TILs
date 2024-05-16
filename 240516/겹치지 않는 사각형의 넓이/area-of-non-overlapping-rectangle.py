arr = [[0]*2000 for _ in range(2000)]

for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = i+1

count1 = 0
for i in arr:
    for j in i:
        if j==1:
            count1+=1

count2 = 0
for i in arr:
    for j in i:
        if j==2:
            count1+=1


print(count1+count2)