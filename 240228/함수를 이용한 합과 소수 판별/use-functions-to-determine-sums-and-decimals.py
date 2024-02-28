def is_prime(n):
    if n==1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False

        return True

def summ(n):
    sum = 0
    l = len(str(n))
    for i in range(l):
        sum += int(str(n)[i])

    return sum

a, b = map(int, input().split())

count = 0
for i in range(a, b+1):
    if is_prime(i) and summ(i)%2==0:
        count += 1

print(count)