def check(s):
    s_li = list(s)
    if s_li == s_li[::-1]:
        print('Yes')
    else:
        print('No')

s = input()
check(s)