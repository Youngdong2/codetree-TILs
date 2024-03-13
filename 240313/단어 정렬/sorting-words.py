n = int(input())
arr = []
for i in range(n):
    arr.append(input())

arr = sorted(arr)
for i in range(n):
    print(arr[i])