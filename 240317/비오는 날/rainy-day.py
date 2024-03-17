class Temp:
    def __init__(self, day, week, weather):
        self.day = day
        self.week = week
        self.weather = weather


n = int(input())
arr = []

for i in range(n):
    day, week, weather = input().split()
    temp = Temp(day, week, weather)
    if temp.weather == 'Rain':
        arr.append(temp)

arr = sorted(arr, key=lambda x: (x.day.split('-')[0], x.day.split('-')[1], x.day.split('-')[2]))

print(f"{arr[0].day} {arr[0].week} {arr[0].weather}")