n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
a1 = []
a2 = []
for i in range(2*n):
    if i%2==0:
        a1.append(arr[i])
    else:
        a2.append(arr[i])

print(max(sum(a1), sum(a2)))