n, m, k = map(int, input().split())
student_penalties = [0]*n


answer = -1

for _ in range(m):
    student_number = int(input())-1
    student_penalties[student_number]+=1
    if student_penalties[student_number] == k:
        answer = student_number + 1
        break

print(answer)