n = int(input())

arr = [input() for _ in range(n)]
result = []
count = 0
for s in arr:
    count += len(s)

result.append(count)

count = 0
for s in arr:
    if s[0]=='a':
        count += 1

result.append(count)

print(' '.join(map(str, result)))