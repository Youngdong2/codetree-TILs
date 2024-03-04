t, m = map(int, input().split())

t = t/100

bmi = int(m / t**2)

print(bmi)
if bmi >= 25:
    print("Obesity")