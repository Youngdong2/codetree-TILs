li = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()

count = 0
for fruit in li:
    if fruit[2]==a or fruit[3]==a:
        print(fruit)
        count += 1

print(count)