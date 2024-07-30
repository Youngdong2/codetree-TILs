arr = [input() for _ in range(10)]

a = input()

count = 0
for s in arr:
    if s[-1]==a:
        print(s)
        count += 1

if count == 0:
    print('None')