def temp(n):
    if n==0:
        return
    temp(n-1)
    print("HelloWorld")

n = int(input())

temp(n)