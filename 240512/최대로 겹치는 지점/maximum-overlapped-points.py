n = int(input())

arr = [0]*200

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, y+1):
        arr[j] += 1

print(max(arr))