def is_number(n):
    return n%2==0

def is_five(n):
    return n%10==5

def is_div(n):
    return n%3==0 and n%9!=0

a, b = map(int, input().split())

count = 0
for i in range(a, b+1):
    if not is_number(i) and not is_five(i) and not is_div(i):
        count+=1

print(count)