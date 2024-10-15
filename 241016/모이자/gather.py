import sys

n = int(input())

arr = list(map(int, input().split()))

max_sum = sys.maxsize

for i in range(1, n+1):
    temp = [abs(i-j)*arr[j] for j in range(len(arr))]
    temp_sum = sum(temp)

    max_sum = min(max_sum, temp_sum)

print(max_sum)