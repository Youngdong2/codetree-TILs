from collections import deque

n = int(input())

q = deque()
for _ in range(n):
    o = input().split()
    if o[0] == "push_back":
        q.append(o[1])
    elif o[0] == "push_front":
        q.appendleft(o[1])
    elif o[0] == "pop_front":
        print(q.popleft())
    elif o[0] == "pop_back":
        print(q.pop())
    elif o[0] == "size":
        print(len(q))
    elif o[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif o[0] == "front":
        print(q[0])

    elif o[0] == "back":
        print(q[-1])