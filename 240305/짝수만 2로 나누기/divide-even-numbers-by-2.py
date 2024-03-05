n = int(input())

li = list(map(int, input().split()))

def temp(li):
    answer = []
    for s in li:
        if s%2==0:
            answer.append(int(s/2))
        else:
            answer.append(s)
    print(' '.join([str(s) for s in answer]))

temp(li)