def check(n):
    if n%4==0:
        return True
    else:
        return False

def exep(n):
    return n%100==0 and n%400!=0

def main(n):
    if check(n) and not exep(n):
        print('true')
    else:
        print('false')

y = int(input())
main(y)