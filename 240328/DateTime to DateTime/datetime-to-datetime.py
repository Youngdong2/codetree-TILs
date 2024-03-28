a, b, c = map(int, input().split())
d = 11
h = 11
m = 11

answer = 0
if a < d or (a==d and b < h) or (a==d and b==h and c < m):
    print(-1)

else:
    while True:
        if d==a and h==b and m==c:
            break
        answer += 1
        m += 1
        if m==60:
            h += 1
            m = 0
        
        if h==24:
            d += 1
            h = 0

    print(answer)