n, k = map(int, input().split())
answer = []

def choose(curr_num):
    if len(answer) == n:
        print(" ".join(map(str, answer)))
        return

    for i in range(1, k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(0)