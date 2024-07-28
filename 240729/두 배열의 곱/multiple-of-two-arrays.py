arr_1 = []
for _ in range(3):
    arr_1d = list(map(int, input().split()))
    arr_1.append(arr_1d)

arr_2 = []
for _ in range(4):
    arr_1d = list(map(int, input().split()))
    arr_2.append(arr_1d)

arr_2 = arr_2[1:]

arr_3 = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr_3[i][j] = arr_1[i][j] * arr_2[i][j]

for row in arr_3:
    print(' '.join(map(str, row)))