n = int(input())
arr = [input() for _ in range(n)]

a = input()

counts = []
for s in arr:
    if s[0]==a:
        counts.append(len(s))

result = []
result.append(len(counts))
average_length = round(sum(counts) / len(counts), 2)
result.append(f"{average_length:.2f}")

print(' '.join(map(str, result)))