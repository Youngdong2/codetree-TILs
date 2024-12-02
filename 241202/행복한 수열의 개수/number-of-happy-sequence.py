n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def has_consecutive(lst, m):
    if not lst:  # 빈 리스트 처리
        return False

    count = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

answer = 0

for i in range(n):
    temp = arr[i]
    if has_consecutive(temp, m):
        answer += 1

for i in range(n):
    temp = [row[i] for row in arr]
    if has_consecutive(temp, m):
        answer += 1    

print(answer)
