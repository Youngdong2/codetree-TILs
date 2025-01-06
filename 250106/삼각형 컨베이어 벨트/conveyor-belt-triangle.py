n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))[::-1]

# Write your code here!
for _ in range(t):
    temp1 = l[-1]
    temp2 = r[-1]
    temp3 = d[0]

    l = [temp3] + l[:n-1]
    r = [temp1] + r[:n-1]
    d = d[1:] + [temp2]

print(*l)
print(*r)
print(*d[::-1])
