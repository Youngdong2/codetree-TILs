n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    j = i-1
    tmp = arr[i]
    while j >= 0 and arr[j] > tmp:
        arr[j+1] = arr[j]
        j = j - 1

    arr[j + 1] = tmp

print(*arr)