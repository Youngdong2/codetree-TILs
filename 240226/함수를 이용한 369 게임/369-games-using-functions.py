def find_bool(n):
    bol = False
    for i in range(len(str(n))):
        if int(str(n)[i])==3 or int(str(n)[i])==6 or int(str(n)[i])==9:
            bol = True
            break
    return bol

def find_3(n):
    return n%3==0


def func(a, b):
    count = 0
    for i in range(a, b+1):
        if find_bool(i) or find_3(i):
            count += 1

    return count


a, b = map(int, input().split())
print(func(a, b))