n, m = map(int, input().split())

x = min(n, m)
answer = 1
for i in range(1, x+1):
    if m%i == 0 and n%i == 0:
        answer = i
        
print(answer)