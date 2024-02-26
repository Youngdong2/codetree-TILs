def is_prime(n):
    if n==1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False

        return True


def main(a, b):
    count = 0
    for i in range(a, b+1):
        if is_prime(i):
            count+=i

    return count

a, b = map(int, input().split())
print(main(a, b))