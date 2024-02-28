def add(a, b):
    return str(a+b)

def diff(a, b):
    return str(a-b)

def multi(a, b):
    return str(a*b)

def div(a, b):
    return str(a//b)

a, oper, b = input().split()

x, y = int(a), int(b)

if oper=='+':
    print(' '.join([a, oper, b, '=', add(x, y)]))

elif oper=='-':
    print(' '.join([a, oper, b, '=', diff(x, y)]))

elif oper=='*':
    print(' '.join([a, oper, b, '=', multi(x, y)]))

elif oper=='/':
    print(' '.join([a, oper, b, '=', div(x, y)]))

else:
    print('False')