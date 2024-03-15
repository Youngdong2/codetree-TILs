class temp:
    def __init__(self, code, site, time):
        self.code = code
        self.site = site
        self.time = time

code, site, time = input().split()
result = temp(code, site, time)

print(f"secret code : {result.code}")
print(f"meeting point : {result.site}")
print(f"time : {result.time}")