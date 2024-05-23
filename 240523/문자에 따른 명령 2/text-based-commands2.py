dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = input()
state = 0
x, y = 0, 0

for i in range(len(arr)):
    if arr[i]=="R":
        state = (state+1)%4
    elif arr[i]=="L":
        state = (state-1)%4
    elif arr[i]=='F':
        x = x + dx[state]
        y = y + dy[state]

print(x, y)