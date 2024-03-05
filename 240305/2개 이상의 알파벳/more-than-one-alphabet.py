def temp(s):
    data = set(list(s))
    if len(data) >= 2:
        print('Yes')
    else:
        print('No')

s = input()
temp(s)