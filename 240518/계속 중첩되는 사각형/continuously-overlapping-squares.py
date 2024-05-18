n = int(input())
arr = [[0]*200 for _ in range(200)]

for i in range(n):
    if i%2==0:
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j][k]=1
    else:
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j][k]=2        


count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==2:
            count += 1

print(count)