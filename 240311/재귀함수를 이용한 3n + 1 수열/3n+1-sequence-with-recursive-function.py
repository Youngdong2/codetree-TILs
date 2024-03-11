def temp(n):
    if n==1:
        return 0

    if n%2==0:
        return temp(n/2)+1
    if n%2==1:
        return temp(n*3+1)+1

n = int(input())
print(temp(n))