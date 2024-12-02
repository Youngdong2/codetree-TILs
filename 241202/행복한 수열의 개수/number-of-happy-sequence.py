n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def has_consecutive(lst, m):
    if not lst:
        return False

    if m == 1:
        return True  # 어떤 원소든 조건을 만족하므로 True 반환

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
