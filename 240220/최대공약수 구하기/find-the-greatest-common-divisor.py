n, m = map(int, input().split())

x = min(n, m)
answer = 0
for i in range(1, x):
    if m%i == 0 and n%i == 0:
        answer = i
        
print(answer)