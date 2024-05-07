n = int(input())

n = str(n)

num = 0
for i in range(len(n)):
    num = 2*num + int(n[i])

print(num)