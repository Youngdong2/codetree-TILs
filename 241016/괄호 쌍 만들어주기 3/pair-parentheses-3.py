string = input()

count = 0
for i in range(len(string)):
    if string[i] == '(':
        for j in range(i+1, len(string)):
            if string[j] == ')':
                count += 1

print(count)