n = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(arr)
arr2 = sorted(arr, reverse=True)

print(max([a+b for a, b in zip(arr1, arr2)]))