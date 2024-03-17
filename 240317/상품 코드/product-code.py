class Temp:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = input().split()

temp1 = Temp('codetree', 50)
temp2 = Temp(name, code)

print(f"product {temp1.code} is {temp1.name}")
print(f"product {temp2.code} is {temp2.name}")