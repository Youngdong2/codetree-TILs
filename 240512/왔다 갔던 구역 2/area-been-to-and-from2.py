n = int(input())

arr = [0]*2000
offset = 1000

for i in range(n):  
    x, d = input().split()
    state = offset
    if d=='R':
        for j in range(state, state+int(x)-1):
            arr[j] += 1

        state = state + int(x)

    else:
        for j in range(state-int(x), state-1):
            arr[j] += 1

        state = state - int(x)

count = 0
for a in arr:
    if a >= 2:
        count += 1

print(count)