m1, d1, m2, d2 = map(int, input().split())

answer = 0
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = m1
d = d1

while True:
    if m==m2 and d==d2:
        break

    answer += 1
    d += 1

    if d > num_of_days[m]:
        m += 1
        d = 1

print(answer)