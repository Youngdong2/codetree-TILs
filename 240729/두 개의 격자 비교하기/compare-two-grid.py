n, m = map(int, input().split())
arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []
for _ in range(n):
    arr2.append(list(map(int, input().split())))

arr3 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            arr3[i][j] = 0
        else:
            arr3[i][j] = 1

for row in arr3:
    print(' '.join(map(str, row)))