def func(n):
    num_1 = int(str(n)[0])
    num_2 = int(str(n)[1])

    if n%2==0 and (num_1+num_2)%5==0:
        print("Yes")
    else:
        print('No')

n = int(input())
func(n)