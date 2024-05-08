n = int(input())

arr = [0 for _ in range(200)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b):
        arr[j] += 1

print(max(arr))