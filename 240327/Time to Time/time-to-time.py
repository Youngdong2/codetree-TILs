a, b, c, d = map(int, input().split())
answer = 0

h = a
m = b

while True:
    if h==c and m==d:
        break

    answer += 1
    m += 1

    if m==60:
        h += 1
        m = 0

print(answer)