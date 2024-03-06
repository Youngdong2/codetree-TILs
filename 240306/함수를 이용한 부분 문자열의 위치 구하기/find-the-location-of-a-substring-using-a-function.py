s1 = input()
s2 = input()


check = False
for i in range(len(s1)-len(s2)+1):
    if s1[i:i+len(s2)] == s2:
        print(i)
        check = True
        break

if check == False:
    print('-1')