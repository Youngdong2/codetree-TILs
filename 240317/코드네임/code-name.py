class temp:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

temp_score = 101

for i in range(5):
    name, score = input().split()
    T = temp(name, score)
    if temp_score > T.score:
        answer = T
        temp_score = T.score

print(f"{answer.name} {answer.score}")