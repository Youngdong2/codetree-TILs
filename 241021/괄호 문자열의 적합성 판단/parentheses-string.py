s = input()

stack = []
for i in range(len(s)):
    if s[i] == "(":
        stack.append(1)
    elif s[i] == ")":
        stack.pop()

if stack:
    print("No")
else:
    print("Yes")