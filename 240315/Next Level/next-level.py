class Temp:
    def __init__(self, ids='codetree', level=10):
        self.ids=ids
        self.level=level

idd, level = input().split()

temp1 = Temp()
temp2 = Temp(idd, level)

print(f"user {temp1.ids} lv {temp1.level}")
print(f"user {temp2.ids} lv {temp2.level}")