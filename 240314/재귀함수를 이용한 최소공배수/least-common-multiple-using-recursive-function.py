def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if i%a==0 and i%b==0:
            return i

n = int(input())
arr = list(map(int, input().split()))

def temp(n):
    if n==0:
        return arr[0]
    
    return lcm(temp(n-1), arr[n])

print(temp(n-1))