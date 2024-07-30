s = input()
a = input()

count = 0
for i in range(len(s)):
    if s[i]==a:
        count += 1

print(count)