class Temp:
    def __init__(self, number, index):
        self.number = number
        self.index = index

n = int(input())
arr = list(map(int, input().split()))

numbers = [Temp(num, i) for i, num in enumerate(arr)]

answer = [0 for _ in range(n)]

numbers.sort(key=lambda x: (x.number, x.index))

for i, number in enumerate(numbers):
    answer[number.index] = i+1

for i in range(n):
    print(answer[i], end=' ')