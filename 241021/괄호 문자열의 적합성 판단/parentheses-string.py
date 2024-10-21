s = input()

def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])

        else:
            if len(stack)==0:
                return False

            stack.pop()

    if stack:
        return False
    
    return True

if check(s):
    print("Yes")
else:
    print("No")