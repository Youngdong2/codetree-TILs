class Temp:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
temp = Temp(code, color, sec)

print(f"code : {temp.code}")
print(f"color : {temp.color}")
print(f"second : {temp.sec}")