n, m, k = map(int, input().split())
student_num = [0]*n


for _ in range(m):
    num = int(input())
    student_num[num-1] += 1


answer = -1
for i in range(n):
    if student_num[i] >= k:
        answer = i+1
        break

print(answer)