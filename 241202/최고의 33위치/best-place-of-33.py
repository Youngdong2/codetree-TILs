n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def count_arr(i, j):
    s = 0
    for m in range(i, i+3):
        for n in range(j, j+3):
            if arr[m][n]==1:
                s += 1

    return s

answer = 0
for i in range(n):
    for j in range(n):
        if i+3 > n or j+3 > n:
            continue
        state = arr[i][j]
        s = count_arr(i, j)
        answer = max(answer, s)

print(answer)


        
        