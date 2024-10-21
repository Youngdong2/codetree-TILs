class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)
        
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items[-1]

n = int(input())

stack = Stack()
for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        stack.push(s[1])
    elif s[0] == 'pop':
        print(stack.pop())
    elif s[0] == 'size':
        print(stack.size())
    elif s[0] == 'empty':
        if stack.empty():
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        print(stack.top())