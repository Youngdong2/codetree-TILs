n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))[::-1]

# Write your code here!
for _ in range(t):
    temp1 = u[-1]
    temp2 = d[0]

    u = [temp2] + u[:n-1]
    d = d[1:] + [temp1]

print(*u)
print(*d[::-1])
