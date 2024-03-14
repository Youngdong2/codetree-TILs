n, k, T = input().split()
n = int(n)
k = int(k)

arr = []
for i in range(n):
    s = input()
    if s.startswith(T):
        arr.append(s)


arr = sorted(arr)
print(arr[k-1])