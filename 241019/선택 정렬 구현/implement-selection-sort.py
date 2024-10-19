n = int(input())

arr = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        min = arr[i]
        if arr[i] > arr[j]:
            min = arr[j]
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(*arr)