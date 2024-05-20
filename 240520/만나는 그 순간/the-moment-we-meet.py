n, m = map(int, input().split())

arr_a = [0]*1000
arr_b = [0]*1000
time = 0
for i in range(n):
    direction, l = input().split()
    l = int(l)
    if direction=='R':
        for j in range(l+1):
            arr_a[time]=arr_a[time-1]+1
            time += 1
    else:
        for j in range(l+1):
            arr_a[time]=arr_a[time-1]-1
            time += 1

time = 0

for i in range(m):
    direction, l = input().split()
    l = int(l)
    if direction=='R':
        for j in range(1, l+1):
            arr_b[time]=arr_b[time-1]+1
            time += 1
    else:
        for j in range(1, l+1):
            arr_b[time]=arr_b[time-1]-1
            time += 1

index_a = 0
for i in range(len(arr_a)-1):
    if abs(arr_a[i+1]-arr_a[i]) != 1:
        index_a = i
        break

index_b = 0
for i in range(len(arr_b)-1):
    if abs(arr_b[i+1]-arr_b[i]) != 1:
        index_b = i
        break
answer=[]
for i in range(min(index_a, index_b)):
    if arr_a[i]==arr_b[i]:
        answer.append(i)
        break
if len(answer)>0:
    print(answer[0])
else:
    print(-1)